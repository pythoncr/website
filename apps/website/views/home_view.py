from apps.website.forms.subscribe_form import SubscribeForm
from apps.website.forms.contact_form import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View


class HomeView(View):

    template = 'website/home.html'

    def get(self, request, *args, **kwargs):

        subscribe_form = SubscribeForm()
        contact_form = ContactForm()

        return render(
            request,
            self.template,
            {
                'subscribe_form': subscribe_form,
                'contact_form': contact_form
            }
        )

    def post(self, request, *args, **kwargs):

        subscribe_form = SubscribeForm()
        contact_form = ContactForm()

        data = request.POST

        if 'subscribe' in data:

            subscribe_form = SubscribeForm(data)

            if subscribe_form.is_valid():

                email = subscribe_form.cleaned_data['email']
                recipients = ['comunidad@python.cr']
                send_mail("Subscribe to comunidad@python.cr", 'subscribe', email, recipients)

        if 'contact' in data:

            contact_form = ContactForm(data)

            if contact_form.is_valid():

                name = contact_form.cleaned_data['name']
                subject = contact_form.cleaned_data['subject']
                message = contact_form.cleaned_data['message']
                sender = contact_form.cleaned_data['sender']

                recipients = ['info@python.cr']

                send_mail(subject+' contacto '+name, message, sender, recipients)

        return render(
            request,
            self.template,
            {
                'subscribe_form': subscribe_form,
                'contact_form': contact_form
            }
        )
