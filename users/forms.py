from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(label='Ad', max_length=50, widget=forms.TextInput(attrs={'class': 'form-controll', 'placeholder': 'Adınız'}), error_messages={'required': 'Adınızı daxil edin'})
    last_name = forms.CharField(label='Soyad', max_length=50, widget=forms.TextInput(attrs={'class': 'form-controll', 'placeholder': 'Soyadınız'}))
    email = forms.EmailField(label='E-mail', max_length=255, widget=forms.EmailInput(attrs={'class': 'form-controll', 'placeholder': 'E-mail ünvanınız'}))
    phone = forms.CharField(label='Telefon', max_length=50, widget=forms.TextInput(attrs={'class': 'form-controll', 'placeholder': 'Telefon nömrəniz',}))
    password = forms.CharField(label='Şifrə', widget=forms.PasswordInput(attrs={'class': 'form-controll', 'placeholder': 'Şifrəniz'}))
    password_conf = forms.CharField(label='Şifrəni təkrar yaz', widget=forms.PasswordInput(attrs={'class': 'form-controll', 'placeholder': 'Şifrənizi yenidən daxil edin'}))


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        qs = User.objects.filter(phone=phone)
        if len(phone) < 10 and len(phone) > 20:
            raise forms.ValidationError("Telefon nömrənizi düzgün daxil edin.")
        if qs.exists():
            raise forms.ValidationError("Bu telefon artıq mövcuddur.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Bu e-mail artıq mövcuddur.")
        return email

    def clean_password_conf(self):
        password = self.cleaned_data.get('password')
        password_conf = self.cleaned_data.get('password_conf')
        print(password, password_conf, self.cleaned_data)
        if len(password) < 8:
            raise forms.ValidationError("Şifrə ən azı 8 simvoldan ibarət olmalıdır.")
        if password != password_conf:
            raise forms.ValidationError("Şifrələr uyğun gəlmir.")



class UserLoginForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=255, widget=forms.EmailInput(attrs={'class': 'form-controll', 'placeholder': 'E-mail ünvanınız'}))
    password = forms.CharField(label='Şifrə', widget=forms.PasswordInput(attrs={'class': 'form-controll', 'placeholder': 'Şifrə'}))

    def clean(self):
        data = super(UserLoginForm, self).clean()
        email = data['email']
        password = data['password']
        qs = User.objects.filter(email=email)
        if qs.exists():
            user = qs.first()
            if not user.check_password(password):
                raise forms.ValidationError("Şifrə yanlışdır.")
        else:
            raise forms.ValidationError("Bu e-mail ünvanına aid istifadəçi tapılmadı.")
        return data

        # password = self.cleaned_data.get('password')
        # password2 = self.cleaned_data.get('password2')
        # if password2 != password:
        #     raise forms.ValidationError("Şifrələr uyğun gəlmir.")
        # return data