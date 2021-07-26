import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'firstproject.settings')
django.setup()

import faker
from baseapp.models import User
fakegen = faker.Faker()


def populate(N=10):
    for i in range(N):
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        email = fakegen.email()
        User.objects.get_or_create(fname=fname, lname=lname, email=email)[0]
populate()
