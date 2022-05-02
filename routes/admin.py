from django.contrib import admin
from .models import Route
# Register your models here.
class RouteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Route Information', {'fields':['origin', 'destination',
        'distance','condition']}),
        ('Cost Information', {'fields': ['cost',
        'filepath', 'calculated_cost', 'cost_status']}),
    ]

admin.site.register(Route, RouteAdmin) 
