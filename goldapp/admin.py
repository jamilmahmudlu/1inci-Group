from django.contrib import admin
from .models import  *
# Register your models here.

# slider
class AddSlider(admin.ModelAdmin):
	list_display = ['title', 'created', 'updated']
admin.site.register(Slider, AddSlider) 
# partnyor
class AddPartnyor(admin.ModelAdmin):
	list_display = ['title', 'created', 'updated']
admin.site.register(Partnyor, AddPartnyor) 

class AddProductSlider(admin.ModelAdmin):
	list_display = ['title', 'created', 'updated']
admin.site.register(ProductSlider, AddProductSlider)

# category admin
admin.site.register(Category)
# product admin
class AddProduct(admin.ModelAdmin):
	list_display = ['name', 'price', 'status', 'created', 'updated']
	list_filter = ['status', 'created', 'updated']
	list_editable = ['price', 'status']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, AddProduct)
# images admin
#ImagesAdmin

class ImagesAdmin(admin.ModelAdmin):
        list_display=['title','product']
        list_display_links = ['title','product']
        search_fields = ['title','product']
admin.site.register(Images,ImagesAdmin)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'telephone')
    list_filter = ('first_name', 'email', 'telephone')
    search_fields = ('first_name', 'email', 'telephone')
