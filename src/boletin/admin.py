from django.contrib import admin
from .forms import RegModelForm
from .models import Registrado


class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timestamp"]
    #list_display_links = ["nombre"]
    form = RegModelForm
    list_filter = ["timestamp",]
    list_editable = ["nombre",]
    search_fields = ["email","nombre"]
    #class Meta:
    #    model = Registrado

# Register your models here.
admin.site.register(Registrado,AdminRegistrado)

