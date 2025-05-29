#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    # Add both the root and project directories to PYTHONPATH
    project_root = Path(__file__).resolve().parent
    project_app_dir = project_root / 'project01'
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(project_app_dir))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project01.settings')
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
