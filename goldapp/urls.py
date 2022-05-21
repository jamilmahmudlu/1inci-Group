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
    path('allproducts', views.allproducts, name="allproducts"),
    path('faq', views.faq, name="faq"),
    path('checkout', views.checkout, name="checkout"),
    path('delivery', views.delivery, name="delivery"),
    path('set-language/', views.change_language, name="set_language"),

]
