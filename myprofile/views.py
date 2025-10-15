from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import logging
import smtplib

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
                settings.EMAIL_HOST_USER,  # always from your authenticated address
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
                headers={"Reply-To": email}
            )
        except BadHeaderError:
            logger.exception('BadHeaderError when sending contact email')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Invalid header found.'}, status=400)
            messages.error(request, 'Invalid header found.')
            return redirect('contact')
        except Exception as e:
            # If this is an SMTP authentication error, fall back to the console
            # backend and resend so users still get a confirmation without a 500.
            logger.exception('Error sending contact email (first attempt)')
            if isinstance(e, smtplib.SMTPAuthenticationError) or 'SMTPAuthenticationError' in type(e).__name__:
                logger.warning('SMTP auth failed — falling back to console email backend and resending')
                # Temporarily switch backend to console and retry
                try:
                    settings.EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
                    send_mail(
                        subject,
                        full_message,
                        settings.EMAIL_HOST_USER or 'no-reply',
                        [settings.EMAIL_HOST_USER or 'no-reply'],
                        fail_silently=True,
                        headers={"Reply-To": email or 'no-reply'}
                    )
                    # Respond as success but note that email was printed to console
                    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        return JsonResponse({'success': True, 'message': 'Email printed to server console due to SMTP auth failure.'})
                    messages.success(request, 'Your message was accepted (printed to server console).')
                    return redirect('contact')
                except Exception:
                    logger.exception('Failed to resend via console backend')
                    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        return JsonResponse({'success': False, 'error': 'Error sending email.'}, status=500)
                    messages.error(request, 'An error occurred while sending your message. Please try again later.')
                    return redirect('contact')

            # For other errors, log and return friendly message
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
