from django import forms

from apps.cliente.models import Persona


class ClienteForm(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
			'rut',
			'nombre',
			'apellido',
			'nacimiento',
			'telefono',
			'email',
		]
		labels = {
			'rut': 'Rut',
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'nacimiento':'Fecha de nacimiento',
			'telefono' : 'Telefono',
			'email' : 'Email',
		}
		widgets = {
			'rut': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}