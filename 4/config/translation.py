from modeltranslation.translator import translator, TranslationOptions
from polls4.models import NewsModel4
class NewsTranslationOptions4(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('uz',)

translator.register(NewsModel4, NewsTranslationOptions4)

 