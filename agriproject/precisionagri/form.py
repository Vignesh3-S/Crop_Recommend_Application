from django import forms
from .models import agriculture
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class agriform(forms.ModelForm):
    district = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'District Name','class':'form-control'}))
    nitrogen = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'Nitrogen Value','class':'form-control'}))
    phosphorus = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'Phosphorus Value','class':'form-control'}))
    potassium = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'Potassium Value','class':'form-control'}))
    temperature = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'Temperature Value','class':'form-control'}))
    humidity = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'Humidity Value','class':'form-control'}))
    ph = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'PH Value','class':'form-control'}))
    rainfall = forms.FloatField(label='',widget=forms.NumberInput(attrs={'placeholder':'Rainfall Value','class':'form-control'}))
    
    class Meta:
        model = agriculture
        fields = ('State_Name',)

class queryform(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Your Name','class':'form-control'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Your Email','class':'form-control'}))
    phone = forms.CharField(label='',widget=forms.NumberInput(attrs={'placeholder':'Your Mobile','class': 'form-control'}))
    message = forms.CharField(label='',widget = forms.Textarea(attrs={'placeholder':'Message','class':'form-control'}))

class loginform(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'UserName','class':'form-control'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
