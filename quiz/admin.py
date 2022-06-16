from django.contrib import admin
from quiz.models import Quiz, Category, Question, Answer

admin.site.register(Quiz)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)