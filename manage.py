#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    # --- START OF AUTOMATIC SUPERUSER CREATION ---
    try:
        from django.contrib.auth import get_user_model
        from django.core.exceptions import ImproperlyConfigured
        
        User = get_user_model()
        
        ADMIN_USER = os.environ.get('ADMIN_USER')
        ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
        ADMIN_PASS = os.environ.get('ADMIN_PASS')

        # Check if all 3 variables are set
        if ADMIN_USER and ADMIN_EMAIL and ADMIN_PASS:
            if not User.objects.filter(username=ADMIN_USER).exists():
                print(f"Creating new superuser: {ADMIN_USER}")
                User.objects.create_superuser(
                    username=ADMIN_USER,
                    email=ADMIN_EMAIL,
                    password=ADMIN_PASS
                )
            else:
                print(f"Superuser {ADMIN_USER} already exists. Skipping.")
        else:
            print("ADMIN env vars not fully set. Skipping superuser creation.")
            
    except ImproperlyConfigured:
        print("DJANGO_SETTINGS_MODULE not set. Skipping superuser creation.")
    except Exception as e:
        # This will catch errors if the database isn't ready, etc.
        print(f"Error during superuser creation: {e}")
    # --- END OF AUTOMATIC SUPERUSER CREATION ---
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()