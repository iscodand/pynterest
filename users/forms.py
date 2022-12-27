from django import forms
from users.models.user import User
from users.validation import Validation


class RegisterForm(forms.ModelForm):
    """ Form to validate and register new users """

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email'
            ]

        password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        password = self.cleaned_data.get('password')
        error_list = dict()
        
        Validation.validate_password(password=password, field_name='password', error_list=error_list)
        
        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)
                
        return self.cleaned_data


class LoginForm(forms.Form):
    """ Form to login users """
    
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
