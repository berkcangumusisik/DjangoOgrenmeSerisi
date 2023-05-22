from django import forms

from .models import Product

# class ProductCreateForm(forms.Form):
#     product_name = forms.CharField(label="Ürün adı", min_length=3, max_length=20, error_messages={
#         "min_length": "min 3 karakter giriniz",
#         "max_length": "mak 20 karakter giriniz"
#     }, widget=forms.TextInput(attrs={'class':'form-control'}))
#     price = forms.DecimalField(label="fiyat", min_value=10, max_value=10000,widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(label="ürün açıklaması",widget=forms.Textarea(attrs={'class':'form-control'}))
#     slug = forms.SlugField(label="url",widget=forms.TextInput(attrs={'class':'form-control'}))

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "price", "description", "slug"]
        error_messages = {
            "product_name": {
                "required": "Ürün adı zorunludur",
                "min_length": "min 3 karakter giriniz",
                "max_length": "mak 50 karakter giriniz"
            },
            "price": {
                "required": "Fiyat zorunludur",
                "min_value": "min 10 TL giriniz",
                "max_value": "mak 100000 TL giriniz"
            },
            "description": {
                "required": "Açıklama zorunludur",
            },
            "slug": {
                "required": "Url zorunludur",
            }
        }
        widgets = {
            "product_name": "Ürün adı",
            "price": "Fiyat",
            "description": "Açıklama",
            "slug": "Url",
        }
        widgets = {
            "product_name": forms.TextInput(attrs={'class':'form-control'}),
            "price": forms.TextInput(attrs={'class':'form-control'}),
            "description": forms.Textarea(attrs={'class':'form-control'}),
            "slug": forms.TextInput(attrs={'class':'form-control'}),
        }