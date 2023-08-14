from django import forms
from goods_map.gallery.models import ImageModel


class ImageForm(forms.ModelForm):
    images = forms.ImageField(localize=2, required=False)

    class Meta:
        model = ImageModel
        fields = ['images']
