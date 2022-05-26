from modeltranslation.translator import register, TranslationOptions

from goldapp.models import Product

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)
