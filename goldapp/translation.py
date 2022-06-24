from modeltranslation.translator import register, TranslationOptions

from goldapp.models import Product, Category

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
