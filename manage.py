#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print(":: SETTINGS MODULE: ", os.environ.get("DJANGO_SETTINGS_MODULE"))
    print("DATABASE_URL: ", os.environ.get("DATABASE_URL"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iigb.settings.dev")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
