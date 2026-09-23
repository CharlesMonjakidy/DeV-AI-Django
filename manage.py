#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devai.settings")

from django.core.management import execute_from_command_line


def main():
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
