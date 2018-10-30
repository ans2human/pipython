from django import forms
from django.utils import timezone
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'startdate', 'employee', 'client', 'description']























#     name = forms.CharField(max_length=25)
#     startdate = forms.DateField(widget=forms.SelectDateWidget())
#     employee = forms.CharField(max_length=24)
#     client = forms.CharField(max_length=25)
#     description = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your description!'
#     )


#     def clean(self):
#         cleaned_data = super(ProjectForm, self).clean()
#         name = cleaned_data.get('name')
#         startdate = cleaned_data.get('date')
#         employee = cleaned_data.get('employee')
#         client = cleaned_data.get('client')
#         description = cleaned_data.get('description')
#         if not name and not employee and not client:
#             raise forms.ValidationError('Bhaiya kuch to detail do')



