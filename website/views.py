from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('Not Valid')

    form = ContactForm()
    return render(request, 'test.html', {'form': form})
