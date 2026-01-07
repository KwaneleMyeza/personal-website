import logging
from django.shortcuts import render, redirect
from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact_view(request):
    sent = False

    try:
        if request.method == "POST":
            form = ContactForm(request.POST)

            if form.is_valid():
                form.save()
                logger.info("Contact message saved successfully.")

                # Prevent duplicate submissions
                return redirect("/contact/?sent=true")

        else:
            form = ContactForm()

        # Detect PRG flag
        if request.GET.get("sent") == "true":
            sent = True

    except Exception as e:
        logger.error(f"Contact form failure: {str(e)}")
        form = ContactForm()
        sent = False

    return render(request,
                  "contact/contact.html",
                  {"form": form, "sent": sent})
