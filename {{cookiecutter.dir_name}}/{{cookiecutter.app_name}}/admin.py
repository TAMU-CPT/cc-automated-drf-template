from django.contrib import admin
from .models import Course, Iteration, Assessment, Result

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class IterationAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'course', 'start_date', 'end_date')

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'iteration', 'start_date', 'end_date')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'assessment', 'submitted', 'score')

admin.site.register(Course, CourseAdmin)
admin.site.register(Iteration, IterationAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Result, ResultAdmin)
