from movies.models import Person, Movies, Role
from django.contrib import admin

# Register your models here.


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mail')

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'director', 'year', 'actors_list')
    
    def actors_list(self, movies):
        return ','.join([str(t) for t in movies.actors.all()])
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'person', 'role')