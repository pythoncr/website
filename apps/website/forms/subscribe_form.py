from django import forms

# Note that it is not inheriting from forms.ModelForm
# We do not need to stored the data

class SubscribeForm(forms.Form):

    email = forms.EmailField(
        label='Correo electrónico',
        max_length=250
    )
