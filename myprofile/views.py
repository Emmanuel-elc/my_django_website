from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import logging

logger = logging.getLogger('myprofile')

def home(request):
    """Render the homepage."""
    return render(request, 'myprofile/home.html')


def projects(request):
    """Render the projects page."""
    return render(request, 'myprofile/projects.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Basic validation
        if not (name and email and subject and message):
            messages.error(request, 'Please fill in all fields before sending.')
            return redirect('contact')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # send to yourself
                fail_silently=False,
            )
        except BadHeaderError:
            logger.exception('BadHeaderError when sending contact email')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Invalid header found.'}, status=400)
            messages.error(request, 'Invalid header found.')
            return redirect('contact')
        except Exception:
            # Log the exception and show a friendly error message instead of a 500
            logger.exception('Error sending contact email')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Error sending email.'}, status=500)
            messages.error(request, 'An error occurred while sending your message. Please try again later.')
            return redirect('contact')

        # Success
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Email sent'})
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'myprofile/contact.html')
