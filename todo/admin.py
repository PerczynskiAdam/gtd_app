from django.contrib import admin
from .models import Case, Action, Result

# Register your models here.
admin.site.register(Case)
admin.site.register(Action)
admin.site.register(Result)