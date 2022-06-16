from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(default='New quiz', max_length=255)
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    )

    TYPE = (
        (0, 'Multiple Choices'),
    )

    quiz = models.ForeignKey(
        Quiz, related_name='quiestion', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name='Type of question')
    title = models.CharField(verbose_name='Title', max_length=255)
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name='Difficulty')
    date_created = models.DateTimeField(
        verbose_name='Date created', auto_now_add=True)
    is_active = models.BooleanField(
        default=False, verbose_name='Active status')

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(verbose_name='Answer text', max_length=255)
    is_right = models.BooleanField(verbose_name='Is correct', default=False)

    def __str__(self):
        return self.answer_text
