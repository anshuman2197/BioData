# def contact(request):
#     contact={'contact':"active"}
#     return render(request,'core/contact.html',contact)# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
# from django.shortcuts import render

# Create your views here.
def home(request):
    context={'home':"active"}
    return render(request,'core/home.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email (you need to configure email settings in Django settings)
            send_mail(
                subject,
                message,
                email,  # From email
                [settings.DEFAULT_FROM_EMAIL],  # To email
                fail_silently=False,
            )
            messages.success(request, "Your Message was Send. :) ")
            return redirect('/') 
            # return render(request,'core/contact.html')  # Redirect to a success page

    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
