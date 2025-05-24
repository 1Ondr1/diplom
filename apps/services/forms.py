from django import forms
from .models import Advertisement, AdImage

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'type', 'description', 'price', 'area']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Назва оголошення'}),
            'type': forms.Select(attrs={'placeholder': 'Тип нерухомості'}),
            'description': forms.Textarea(attrs={'placeholder': 'Опис', 'class': 'form-desc'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ціна за місяць', 'min': 1}),
            'area': forms.NumberInput(attrs={'placeholder': 'Площа (м²)', 'min': 1}),
        }
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Ціна має бути більше 0.")
        return price

    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area is not None and area <= 0:
            raise forms.ValidationError("Площа має бути більше 0.")
        return area

class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ['image', 'advertisement']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'advertisement' not in self.initial:
            self.initial['advertisement'] = self.instance.advertisement
