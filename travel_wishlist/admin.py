from django.contrib import admin
from .models import Place, CatFact

admin.site.register(Place)  # Registers Place model
admin.site.register(CatFact)
