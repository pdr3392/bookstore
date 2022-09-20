import signal
from time import sleep
import os

os.system("poetry run python manage.py runserver 8000")
sleep(60)
os.kill(signal.SIGINT)
