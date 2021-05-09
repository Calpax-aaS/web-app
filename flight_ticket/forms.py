from django.forms import ModelForm, TextInput

from flight_ticket.models import Category, LeadOrigin


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color', 'size': 10}),
            'background_color': TextInput(attrs={'type': 'color', 'size': 10}),
        }


class LeadOriginForm(ModelForm):
    class Meta:
        model = LeadOrigin
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color', 'size': 10}),
            'background_color': TextInput(attrs={'type': 'color', 'size': 10}),
        }