import os
import sys
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from django.conf import settings
from django.core.mail import send_mail

print('EMAIL_HOST:', settings.EMAIL_HOST)
print('EMAIL_PORT:', settings.EMAIL_PORT)
print('EMAIL_USE_TLS:', settings.EMAIL_USE_TLS)
print('EMAIL_HOST_USER:', repr(settings.EMAIL_HOST_USER))
print('EMAIL_HOST_PASSWORD:', '***' if settings.EMAIL_HOST_PASSWORD else '(empty)')

try:
    result = send_mail(
        'Test email from local script',
        'This is a test message from send_test_email.py',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
    print('send_mail returned:', result)
except Exception:
    print('Exception during send_mail:')
    traceback.print_exc()
    sys.exit(1)
