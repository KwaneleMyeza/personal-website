from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    # Honeypot
    nickname = forms.CharField(required=False)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    # Extra validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name.strip()) < 2:
            raise forms.ValidationError("Name too short.")
        return name

    def clean_message(self):
        msg = self.cleaned_data.get('message')

        if len(msg.strip()) == 0:
            raise forms.ValidationError("Message cannot be empty.")

        if len(msg) > 2000:
            raise forms.ValidationError("Message too long (max 2000 characters).")

        return msg

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError("Email is required.")

        if "@" not in email:
            raise forms.ValidationError("Enter a valid email address.")

        return email

    def clean_nickname(self):
        # If honeypot filled 
        if self.cleaned_data.get('nickname'):
            raise forms.ValidationError("Spam detected.")
        return self.cleaned_data.get('nickname')
