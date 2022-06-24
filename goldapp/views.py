from itertools import product
from sys import prefix
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
def index(request):
    mainproducts = Product.objects.filter(is_mainpage=True)
    dateproducts = Product.objects.order_by('-id')[:8]
    slide=Slider.objects.all()
    engslide = EnglishSlider.objects.all()
    # paginator=Paginator(mainproducts,1)
    page=request.GET.get('page')
    # newproducts=paginator.get_page(page)
    partnyor=Partnyor.objects.all()
    context={
        'dateproduct':dateproducts,
        "mainproduct":mainproducts,
        "slide":slide,
        "engslide": engslide,
        "partnyor":partnyor,
    }
    return render(request, 'index.html',context)


def allproducts(request):
    products_ = Product.objects.all()
    paginator = Paginator(products_, 20)
    page = request.GET.get('page')
    prod_slide = ProductSlider.objects.all()
    products = paginator.get_page(page)
    context = {
        'product':products,
        "prod_slide":prod_slide,
    }
    return render(request, "allproducts.html", context=context)


def about(request):

    return render(request, 'about.html')


def get_product(request,id):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    page = request.GET.get('page')
    #yorumları getirme
    context = {
        'product':product,
        'category':category,
        'images':images,
    }

    return render(request,"product.html",context=context)


# category
def get_products(request):
    # products = Product.objects.all()
    product_ = Product.objects.all()
    paginator = Paginator(product_, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    # products=Product.objects.filter()
    return render(request, "category.html", {"prodcut":products})

# katoqoriyadakı paginton tıklayanda ona uyğun göstərir
def get_product_category(request, id):
    product_ = Product.objects.filter(category_id=id)
    paginator = Paginator(product_, 8)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request, "category.html", {"product":product})


def contact(request):

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goldapp:contact')
        else:
            print(form.errors)
    else:
        form = ContactUsForm()

    context = {
        'title' : 'Contact Us',
        'form' : form,
    }

    return render(request, "contact.html", context=context)


def faq(request):
    faqs = Faq.objects.all()
    context ={
        'faqs': faqs
    }
    return render(request, "faq.html", context)


def checkout(request):
    return render(request, 'checkout.html')


def delivery(request):
    return render(request, 'delivery.html')


def change_language(request):
    if request.GET.get('lang') == 'az' or request.GET.get('lang') == 'en' or request.GET.get('lang') == 'default':
        # print(request.META.get('HTTP_REFERER'))
        path_list = request.META.get('HTTP_REFERER').split('/')
        # print(path_list)
        
        if request.GET.get('lang') == 'default':
            path_list.pop(3)
        else:
            path_list.insert(3, request.GET.get('lang'))
        path = '/'.join(path_list)
        # print(path)
        
        response = HttpResponseRedirect(path)
        response.set_cookie('django_language', request.GET['lang'])
        return response