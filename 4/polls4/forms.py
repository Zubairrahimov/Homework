from django import forms
from polls4.models import NewsModel4
class NewsForm4(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_en = forms.CharField()
    task_name_ru = forms.CharField()

    description_uz = forms.CharField()
    description_en = forms.CharField()
    description_ru = forms.CharField()


    class Meta:
        model = NewsModel4
        exclude = ('title', 'body') 