from django import forms
from .models import User,Room
from django.db import models
from django.forms import ModelForm,TextInput,Textarea,RadioSelect,Select
from django.forms import widgets

class UserForm(forms.ModelForm):
	

	class Meta:
		model = User
		fields = ('login','IdRoom','password',)
		labels = {
		'IdRoom': '',
		'login':'',
		'password':'',
		}
		widgets = {
		'password': TextInput(attrs= {'required':'true',
			'type':'password',
			'autocomplete':'off',
			'class':'passwd',
			'placeholder':'PASSWORD',
			}),

		'login':TextInput(attrs= {'required':'true',
			'autocomplete':'off',
			'class':'login',
			'placeholder':'LOGIN'}),

		'IdRoom': RadioSelect(attrs={'class':'Room-select'}),
		}

	
