from modeltranslation.translator import translator, TranslationOptions
from polls5.models import NewsModel5

class NewsTranslationOptions5(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('uz',)

translator.register(NewsModel5, NewsTranslationOptions5)

 