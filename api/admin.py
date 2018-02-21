from django.contrib import admin

from api.models import Customer, Locality, Scrapyard, Transport, Email, Setting

admin.site.register(Customer)
admin.site.register(Locality)
admin.site.register(Scrapyard)
admin.site.register(Transport)
admin.site.register(Email)
admin.site.register(Setting)
