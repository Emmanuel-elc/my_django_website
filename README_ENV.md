Local environment variables for sending email
==========================================

This project reads `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` from the environment.
For local development, you can either create a `.env` file (not committed) or set the variables in PowerShell.

PowerShell (temporary, for current session):

```powershell
$env:EMAIL_HOST_USER = 'youremail@gmail.com'
$env:EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
python manage.py runserver
```

To create a local `.env` file (recommended for convenience):

1. Copy `.env.example` to `.env`.
2. Fill in your real values.

Note: By default this repo uses the `python-dotenv` pattern via `python.envFile` in `.vscode/settings.json` only for convenience in development. Do not commit `.env` to git.

Production: set the same variables in your hosting provider's environment settings (Render, Heroku, etc.).

Security:
- Do not store real passwords in source control.
- For Gmail, enable 2FA and create an App Password to use as `EMAIL_HOST_PASSWORD`.
