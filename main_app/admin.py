from django.contrib import admin
from main_app.models import Research, Member, Contact, Publication, People, Faculty

# Register your models here.

admin.site.register(Research)
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Publication)
admin.site.register(People)
admin.site.register(Faculty)
