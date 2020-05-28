from django.contrib import admin
from .models import Event, EventData, EventDetail, Person


class EventDataAdmin(admin.ModelAdmin):
    search_fields = ['runner']

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['last_name']
admin.site.register(Person, PersonAdmin)
admin.site.register(Event)
admin.site.register(EventData, EventDataAdmin)
admin.site.register(EventDetail)
