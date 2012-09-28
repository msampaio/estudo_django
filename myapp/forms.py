from django.forms.models import ModelForm
from myapp.models import MyModel

class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
