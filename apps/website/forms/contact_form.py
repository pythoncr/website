from django import forms

# Note that it is not inheriting from forms.ModelForm
# We do not need to stored the data

class ContactForm(forms.Form):

    name = forms.CharField(
        label='Nombre',
        max_length=80
    )

    sender = forms.EmailField(
        label='Correo electrónico'
    )

    subject = forms.CharField(
        label='Asunto',
        max_length=250
    )

    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea,
    )
