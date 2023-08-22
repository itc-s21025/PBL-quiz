from django.contrib import admin

from question.models import Question, Choice, Category, Choice2, Question2, Question3, Question4, Question5, Choice3, \
    Choice4, Choice5, QuizResult, Question6, Choice6

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)
admin.site.register(Choice2)
admin.site.register(Question2)
admin.site.register(Question3)
admin.site.register(Question4)
admin.site.register(Question5)
admin.site.register(Question6)
admin.site.register(Choice3)
admin.site.register(Choice4)
admin.site.register(Choice5)
admin.site.register(Choice6)
admin.site.register(QuizResult)