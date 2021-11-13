from django.contrib import admin
from .models import Quiz,Answer,Question, SaveAns,Result

# Register your models here.
admin.site.register(Quiz)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(SaveAns)
admin.site.register(Result)