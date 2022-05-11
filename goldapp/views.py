from itertools import product
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
# Create your views here.
def index(request):
    newproducts_ = Product.objects.all()
    slide=Slider.objects.all()
    prod_slide = ProductSlider.objects.all()
    paginator=Paginator(newproducts_,12)
    page=request.GET.get('page')
    newproducts=paginator.get_page(page)
    partnyor=Partnyor.objects.all()
    context={
        "newproduct":newproducts,
        "slide":slide,
        "prod_slide":prod_slide,
        "partnyor":partnyor
    }
    return render(request, 'index.html',context)
# About
def about(request):

    return render(request, 'about.html')
# Contact
# def contact(request):
#     return render(request, 'contact.html')
# def get_product(request,id):
#     product = get_object_or_404(Product, id=id) 
#     rproduct = Product.objects.filter(category_id=product.category.id)
#     page = request.GET.get('page')
#     context = {
#         "product":product,
#         "rproduct": rproduct,
#     }
#     return render(request, "product.html", context)
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


# email

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('full-name')
#         email = request.POST.get('email')
#         number = request.POST.get('number')
#         message = request.POST.get('message')
#         data = {
#             'name': name,
#             'email': email,
#             'number': number,
#             'message': message
#         }
#         message = '''
#           Yeni Message: {}

#           From: {}
#           Nömrə: {}
          
#           '''.format(data['message'],data['email'],data['number'])

#         send_mail(data['name'] ,message, '', ['jamilmahmudlu@gmail.com'])
#         return render(request,'contact.html')
#     return render(request, 'contact.html', {})

