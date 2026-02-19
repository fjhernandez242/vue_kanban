from django.contrib import admin
from .models import tablero_model

# Register your models here.
class TableroModelAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista del panel
    list_display = ('guia', 'cliente', 'lista')
    # Añade un campo de búsqueda
    search_fields = ['guia', 'cliente']
    # Añade filtros en la barra lateral
    list_filter = ('lista', 'cliente')

# Ahora registra tu modelo con la clase personalizada
admin.site.register(tablero_model, TableroModelAdmin)