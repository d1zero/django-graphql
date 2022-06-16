import graphene
from quiz.models import Quiz, Category, Question, Answer
from quiz.types import QuizType, QuestionType, AnswerType, CategoryType


class Query(graphene.ObjectType):
    all_quizzes = graphene.List(QuizType)
    quiz_by_id = graphene.Field(QuizType, id=graphene.Int())
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, question_id=graphene.Int())

    def resolve_all_quizzes(root, info):
        return Quiz.objects.all()

    def resolve_quiz_by_id(root, info, id):
        return Quiz.objects.get(pk=id)

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, question_id):
        return Answer.objects.filter(question__id=question_id)


schema = graphene.Schema(query=Query)
