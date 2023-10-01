from django import forms
from myapp.models import Employee


class MyForm(forms.ModelForm):
    class Meta: 
        model =  Employee
        fields = ["fullname","mobile"]
        labels = {"fullname":"Name","mobile":"Mobile Number"}