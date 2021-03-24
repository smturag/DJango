from django.forms import ModelForm
from .models import user_info

class user_form(ModelForm):
    class Meta:
        model = user_info
        fields = ["name","age"]

