from django import forms
from record.models import Diary

class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        fields = ['calorie', 'exercise', 'exerciseTime', 'comment']
