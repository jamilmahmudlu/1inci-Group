from django.shortcuts import render
from django.db.models import Q
from goldapp.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
def search(request):
	search = request.GET.get('q')
	products = Product.objects.all()
	if search:
		products = products.filter(
			Q(name__icontains=search)

		)
	paginator = Paginator(products, 8)
	page = request.GET.get('page')
	products = paginator.get_page(page)
	context = {
		"product": products,
		"search": search,
	}
	return render(request, 'category.html', context)