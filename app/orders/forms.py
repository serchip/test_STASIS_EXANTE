from django import forms
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.Form):
    email = forms.EmailField(label=_("Email"), required=True)
    first_name = forms.CharField(label=_("Имя"), max_length=150, required=False)
