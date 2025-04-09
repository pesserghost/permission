from django.contrib import admin
from .models import Teacher, Course, Lesson

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)