from django import forms
from django.core import validators

# def check_for_z(name):
#     if name[0].lower != 'z':
#         raise forms.ValidationError("First char is not Z")

class Form(forms.Form):
    fname = forms.CharField(validators=[check_for_z])
    lname = forms.CharField()
    email = forms.CharField()
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Hidden Input got a botch")
    #     return botcatcher
    def clean(self):
        super().clean()
