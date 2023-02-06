from django import forms

from django.core import validators

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name is started with a')

def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('len is too low')


class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    reemail=forms.EmailField(max_length=100)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reemail']
        if e!=r:
            raise forms.ValidationError('not matched')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot is catched')




