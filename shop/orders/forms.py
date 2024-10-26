from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Имя"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Фамилия"}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Номер телефона 8(XXX)-XXX-XX-XX"}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit() or len(phone_number) != 11 :
            raise forms.ValidationError("Неверный формат номера")
        
        return phone_number