from modeltranslation.translator import translator, TranslationOptions
from polls1.models import NewsModel1

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('uz',)

translator.register(NewsModel1, NewsTranslationOptions)

 