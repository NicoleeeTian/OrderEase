from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        # super(): This is a built-in Python function that allows you to call methods
        # from the parent class. In the case of super(UserForm, self).clean(), 
        # it's calling the clean() method of the parent class of UserForm. 
        # This is important in Django forms because the parent class's clean() method 
        # handles some default validation and cleaning of form data.
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        