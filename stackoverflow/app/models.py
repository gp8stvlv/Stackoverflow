from django.contrib.auth.models import User
from django.db.models import Count
from django.db import models


class ProfileManager(models.Manager):
    def get_top_five_profiles(self):
        return self.order_by('-rating')[:5]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    rating = models.IntegerField(default=0)

    objects = ProfileManager()

    def __str__(self):
        return f'{self.user.username} - Rating: {self.rating}' #Этот метод выводит строку, представляющую профиль пользователя, включая имя пользователя и рейтинг.

class TagManager(models.Manager):
    def get_top_five_tags(self):
        return self.annotate(count=Count('questions')).order_by('-count')[:5]

    def get_by_question(self, question):
        return self.filter(questions=question)

    def get_by_title(self, current_title):
        return self.filter(title=current_title)

#  Сортировка по рейтингу вопроса.
class Tag(models.Model):
    title = models.CharField(max_length=30)

    objects = TagManager()

    def __str__(self):
        return self.title  #Выводит просто заголовок тега.


class QuestionManager(models.Manager):
    def sort_by_date(self):
        return self.order_by('create_date')
    
    def sort_by_rating(self):
        return self.order_by('rating')

#  сортировка по дате добавления и рейтингу (2 вида сортировки).
class Question(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='questions')
    tags = models.ManyToManyField('Tag', related_name='questions')

    objects = QuestionManager()

    def __str__(self):
        return f'{self.title} - Rating: {self.rating}'  #Выводит строку, представляющую вопрос, включая заголовок и рейтинг.

# Ответы сортируются по рейтингу и дате добавления при равном рейтинге.
class Answer(models.Model):
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f'Answer to "{self.question.title}" by {self.profile.user.username}' #Выводит строку, представляющую ответ, включая заголовок вопроса, к которому относится ответ, и имя пользователя, который дал ответ.

class LikeManager(models.Manager):
    def sort_by_rating_and_date(self):
        return self.order_by('-question__rating', 'create_date')

class Like(models.Model):
    LIKE_CHOICES = [
        ('+', 'Like'),
        ('-', 'Dislike'),
    ]

    type = models.CharField(max_length=1, choices=LIKE_CHOICES, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='likes')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='likes')

    objects = LikeManager()

    def __str__(self):
        return f'{self.profile.user.username} {self.get_type_display()} to "{self.question.title}"' #Выводит строку, представляющую лайк, включая имя пользователя, тип лайка (+ или -) и заголовок вопроса, к которому относится лайк.