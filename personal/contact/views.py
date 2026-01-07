from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    sent = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()        # <<< THIS saves to DB
            sent = True
            form = ContactForm()   # clear form after sending
    else:
        form = ContactForm()

    return render(request,
                  'contact/contact.html',
                  {'form': form, 'sent': sent})
