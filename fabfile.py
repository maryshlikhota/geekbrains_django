import os
from fabric.api import local
from importlib import find_loader, __import__


REQUIRENMENTS_FILE_PATH = 'requirenments.pip'

def runserver(*args):
    local(f'cd myshop; python manage.py runserver {" ".join(args)}')


def startapp(*args):
    local(f'cd myshop; python manage.py startapp {" ".join(args)}')


def makemigrations(*args):
    local(f'cd myshop; python manage.py makemigrations {" ".join(args)}')


def migrate(*args):
    local(f'cd myshop; python manage.py migrate {" ".join(args)}')


def collectstatic(*args):
    local(f'cd myshop; python manage.py collectstatic {" ".join(args)}')


def createsuperuser(*args):
    local(f'cd myshop; python manage.py createsuperuser {" ".join(args)}')


def install(module_name=None, *args):
    if not module_name:
        local(f'pip install -r {REQUIRENMENTS_FILE_PATH}')
    else:
        local(f'pip install {module_name} {" ".join(args)}')
        local(f'pip freeze > {REQUIRENMENTS_FILE_PATH}')


def init():
    if not os.path.exists(REQUIRENMENTS_FILE_PATH):
        local(f'pip freeze > {REQUIRENMENTS_FILE_PATH}')
