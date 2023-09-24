from modeltranslation.translator import translator, TranslationOptions
from polls3.models import NewsModel3

class NewsTranslationOptions3(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('uz',)

translator.register(NewsModel3, NewsTranslationOptions3)
