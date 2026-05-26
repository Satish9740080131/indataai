from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Testimonial, Service, FAQ, NewsletterSubscriber, Portfolio, Event, QuoteRequest
from .forms import ContactForm, QuoteRequestForm


def handle_newsletter(request):
    if request.method == 'POST' and 'newsletter' in request.POST:
        email = request.POST.get('email', '').strip()
        if email:
            try:
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            except IntegrityError:
                messages.info(request, 'You are already subscribed with this email.')
        else:
            messages.error(request, 'Please enter a valid email address.')
        return True
    return False


def home(request):
    if handle_newsletter(request):
        return redirect('home')
    context = {
        'testimonials': Testimonial.objects.filter(is_active=True)[:3],
        'services': Service.objects.filter(is_active=True)[:4],
        'page': 'home',
    }
    return render(request, 'website/home.html', context)


def about(request):
    if handle_newsletter(request):
        return redirect('about')
    return render(request, 'website/about.html', {'page': 'about'})


def services(request):
    if handle_newsletter(request):
        return redirect('services')
    return render(request, 'website/services.html', {
        'services': Service.objects.filter(is_active=True),
        'page': 'services',
    })


def faq(request):
    if handle_newsletter(request):
        return redirect('faq')
    return render(request, 'website/faq.html', {
        'faqs': FAQ.objects.filter(is_active=True),
        'page': 'faq',
    })


def testimonial(request):
    if handle_newsletter(request):
        return redirect('testimonial')
    return render(request, 'website/testimonial.html', {
        'testimonials': [],
        'page': 'testimonial',
    })


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        if handle_newsletter(request):
            return redirect('contact')
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent! We will get back to you soon.')
            return redirect('contact')
    return render(request, 'website/contact.html', {
        'contact_form': contact_form,
        'page': 'contact',
    })


def portfolio(request):
    if handle_newsletter(request):
        return redirect('portfolio')
    return render(request, 'website/portfolio.html', {
        'portfolios': Portfolio.objects.filter(is_active=True),
        'page': 'portfolio',
    })


def event(request):
    if handle_newsletter(request):
        return redirect('event')
    return render(request, 'website/event.html', {
        'events': Event.objects.filter(is_active=True),
        'page': 'event',
    })


def request_quote(request):
    quote_form = QuoteRequestForm()
    if request.method == 'POST':
        if handle_newsletter(request):
            return redirect('request_quote')
        quote_form = QuoteRequestForm(request.POST)
        if quote_form.is_valid():
            quote_form.save()
            messages.success(request, 'Your quote request has been sent! We will evaluate and get back to you soon.')
            return redirect('request_quote')
    return render(request, 'website/quote.html', {
        'quote_form': quote_form,
        'page': 'quote',
    })
