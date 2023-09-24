from django import forms
from polls5.models import NewsModel5
class NewsForm5(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_en = forms.CharField()
    task_name_ru = forms.CharField()

    description_uz = forms.CharField()
    description_en = forms.CharField()
    description_ru = forms.CharField()


    class Meta:
        model = NewsModel5
        exclude = ('title', 'body') 