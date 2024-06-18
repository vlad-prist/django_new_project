from django.contrib import admin
from new_app.models import Student, Subject


# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'students',)
    search_fields = ('students',)
