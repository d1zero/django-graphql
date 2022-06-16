from graphene_django import DjangoObjectType
from quiz.models import Quiz, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'category')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text')
