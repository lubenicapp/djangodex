#!/usr/bin/env python
import os
import sys
import time

from django.db import connections

# Wait for the database to become available
def wait_for_db():
    db_conn = None
    while not db_conn:
        try:
            db_conn = connections['default']
        except Exception as e:
            print("Waiting for database...")
            time.sleep(1)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangodex.settings")
    wait_for_db()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
