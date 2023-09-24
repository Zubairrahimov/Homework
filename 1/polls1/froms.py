from django import forms
from polls1.models import NewsModel1
class NewsForm(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_en = forms.CharField()
    task_name_ru = forms.CharField()

    description_uz = forms.CharField()
    description_en = forms.CharField()
    description_ru = forms.CharField()


    class Meta:
        model = NewsModel1
        exclude = ('title', 'body') 