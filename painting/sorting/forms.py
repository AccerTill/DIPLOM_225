from django.forms import ModelForm
from .models import Shop, Feedbackall
from django import forms


class FeedbackallForm(ModelForm):
    class Meta:
        model = Feedbackall
        fields = ['name', 'text']



class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'picture', 'author', 'genre', 'size', 'price']


        # widgets = {
        #     'genre': forms.EmailField(),
        # }
    #
    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #
    #         for name, field in self.fields.items():
    #             field.widget.attrs.update({'class':'form_field'})

            # self.fields['name'].widget.attrs.update({'class':'form_field'})
            # self.fields['picture'].widget.attrs.update({'class':'form_field'})
            # self.fields['author'].widget.attrs.update({'class':'form_field'})
            # self.fields['genre'].widget.attrs.update({'class':'form_field'})
            # self.fields['size'].widget.attrs.update({'class':'form_field'})
            # self.fields['price'].widget.attrs.update({'class':'form_field'})














