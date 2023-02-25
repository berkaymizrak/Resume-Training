from django import forms
from django.conf import settings
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=254,
        required=True,
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
    )
    subject = forms.CharField(
        max_length=254,
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )

    def send_mail(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']
            message_context = 'Message received.\n\n' \
                              'Name: %s\n' \
                              'Subject: %s\n' \
                              'Email: %s\n' \
                              'Message: %s' % (name, subject, email, message)

            # Send email here
            email = EmailMessage(
                subject,
                message_context,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )
            email.send()
