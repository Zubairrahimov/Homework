from django import forms
from polls2.models import NewsModel2
class NewsForm2(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_en = forms.CharField()
    task_name_ru = forms.CharField()

    description_uz = forms.CharField()
    description_en = forms.CharField()
    description_ru = forms.CharField()


    class Meta:
        model = NewsModel2
        exclude = ('title', 'body') 