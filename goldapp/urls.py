from django.urls import path
from . import views

app_name = 'goldapp'

urlpatterns = [
	path('', views.index, name = "index"),
	path('product/<int:id>', views.get_product, name="product"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('products', views.get_products, name="products"),
    path('category/<int:id>', views.get_product_category, name="category"),
]
