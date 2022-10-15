from django.contrib import admin

# Register your models here.

from Registration.models import Course, Batch, Student
# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Student)
