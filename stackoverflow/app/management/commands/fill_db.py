# app/management/commands/fill_db.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Tag, Question, Answer, Like
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Coefficient for data filling')

    def handle(self, *args, **options):
        ratio = options['ratio']
        fake = Faker()

        users_count = ratio
        tags_count = ratio
        question_count = ratio * 10
        answers_count = ratio * 100
        likes_count = ratio * 200

        # # Create Users
        # users = []
        # for i in range(users_count):
        #     username = f"{fake.user_name()}{i}"
        #     email = f"{fake.email()}{i}"
        #     user = User.objects.create_user(username=username,
        #                                     first_name=fake.first_name(),
        #                                     last_name=fake.last_name(),
        #                                     email=email,
        #                                     password=fake.password())
        #     users.append(user)

        # self.stdout.write("Users filled\n")
        # # Create Profiles
        # avatars = ["user_avatar1.png", "user_avatar2.png", "user_avatar3.jpeg", "user_avatar4.png", "user_avatar5.png"]
        # avatars = [f"static/images/avatars/{avatar}" for avatar in avatars]

        # for user in users:
        #     avatar = random.choice(avatars)  # случайное изображение из списка
        #     Profile.objects.create(user=user, avatar=avatar, rating=random.randint(1, 100))
            
        # self.stdout.write("Profiles filled\n")
            
        # # Create Tags
        # tags = []
        # for i in range(tags_count):
        #     tag = Tag.objects.create(title=fake.word())
        #     tags.append(tag)

        # self.stdout.write("Tags filled\n")

        # # Create Questions
        # for i in range(question_count):
        #     question = Question.objects.create(
        #         title=fake.sentence()[:40],
        #         body=fake.text()[:150],
        #         create_date=fake.date_time_this_decade(),
        #         rating=random.randint(-100, 100),
        #         profile=random.choice(Profile.objects.all())
        #     )
        #     question.tags.set(random.sample(tags, random.randint(1, 3)))

        # self.stdout.write("Questions filled\n")

        # Create Answers
        for i in range(answers_count):
            answer = Answer.objects.create(
                body=fake.text()[:30],
                create_date=fake.date_time_this_decade(),
                is_correct=random.choice([True, False]),
                profile=random.choice(Profile.objects.all()),
                question=random.choice(Question.objects.all())
            )

        self.stdout.write("Answers filled\n")

        # Create Likes
        for i in range(likes_count):
            Like.objects.create(
                type=random.choice(['+', '-']),
                profile=random.choice(Profile.objects.all()),
                question=random.choice(Question.objects.all())
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully filled the database with test data.'))
