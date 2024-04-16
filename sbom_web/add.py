import os
import django
from sbom_app.models import Person

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sbom_app.settings")
django.setup()

person = Person(first_name='John', last_name='Doe')
person.save()
