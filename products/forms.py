from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["image", "image_alt", "title", "description", "dimensions", "category", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Titre de la publication",
                "class": "input-text",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Décrivez le produit, son état, son usage...",
                "rows": 4,
                "class": "input-textarea",
            }),
            "dimensions": forms.TextInput(attrs={
                "placeholder": "Ex: 120 x 80 x 60 cm",
                "class": "input-text",
            }),
            "image_alt": forms.TextInput(attrs={
                "placeholder": "Texte alternatif pour la photo",
                "class": "input-text",
            }),
            "category": forms.Select(attrs={
                "class": "input-select",
            }),
        }

