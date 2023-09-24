from modeltranslation.translator import translator, TranslationOptions
from polls2.models import NewsModel2

class NewsTranslationOptions2(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('uz',)

translator.register(NewsModel2, NewsTranslationOptions2)

 