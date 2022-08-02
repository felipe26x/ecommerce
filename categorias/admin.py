from django.contrib import admin
from .models import category

# Register your models here.


# manejo del slug 'referencias para las categorias , creamos una clase 
# y a esa clase le pasamos un parametro que es el modelo del administrador
# accedemos a una de sus propiedades 'prepopulated_fields' 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')


admin.site.register(category , CategoryAdmin)
