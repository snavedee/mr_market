#!/usr/bin/env python
import os
import sys
import django
import traceback

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mr_makeit.settings')
    print("Apps loading...")
    try:
        django.setup()
    except Exception as e:
        print("Exception during setup:")
        traceback.print_exc()
        raise
    print("Apps loaded.")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()