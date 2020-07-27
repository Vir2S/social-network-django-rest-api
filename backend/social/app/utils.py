# Developed by Vitaly Sem

from django.conf import settings
from pyhunter import PyHunter

e_hunter = PyHunter(settings.HUNTER_API_KEY)
