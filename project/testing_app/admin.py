from django.contrib import admin
from .models import Student, Test, TestResult

admin.site.register(Student)
admin.site.register(Test)
admin.site.register(TestResult)

