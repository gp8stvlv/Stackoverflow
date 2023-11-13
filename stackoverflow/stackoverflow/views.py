import random
from django.shortcuts import render

IS_AUTH = False

QUESTIONS = [
        {
            'id': i,
            'title': f'question number {i}',
            'body': f'this is a very very long question... that has {i} id',
            'tags': 'new tag',
            'answer_count': 1,
            'like_count': 2
        }  for i in range(10)
    ]

POPULAR_TAGS = [
    {'id': 1, 'name': 'perl'},
    {'id': 2, 'name': 'python'},
    {'id': 3, 'name': 'techopark'},
    {'id': 4, 'name': 'mySQL'},
    {'id': 5, 'name': 'django'},
    {'id': 6, 'name': 'Mail.ru'},
    {'id': 7, 'name': 'Voloshin'},
    {'id': 8, 'name': 'FireFox'}
]

BEST_MEMBERS = [
    {'id': 1, 'name': 'Mr. Freeman'},
    {'id': 2, 'name': 'V. Pupkin'},
    {'id': 3, 'name': 'Ivanov'},
]

TAGS = [
    {'id': 1, 'name': 'perl'},
    {'id': 2, 'name': 'python'},
    {'id': 3, 'name': 'techopark'},
    {'id': 4, 'name': 'mySQL'},
    {'id': 5, 'name': 'django'},
    {'id': 6, 'name': 'Mail.ru'},
    {'id': 7, 'name': 'Voloshin'},
    {'id': 8, 'name': 'FireFox'},
    {'id': 9, 'name': ''},
    {'id': 10, 'name': 'new tag'},
    {'id': 11, 'name': 'pandas'},
    {'id': 12, 'name': 'large-datasets'}
]

ANSWERS = [
            {
            'id': i,
            'title': f'{i} answer',
            'body': """Empowering the world to develop technology through collective knowledge.
                Our public platform serves millions of people every month, making it one of the most popular
                websites in the world.
                Our asynchronous knowledge management and collaboration offering, Stack Overflow for Teams, is
                transforming how people work.""",
            'is_correct': True
        }  for i in range(15)
]

def tag(request, tag_name):
    tag_request = None
    for tag in TAGS:
        if tag['name'] == tag_name:
            tag_request = tag
            break

    return render(request, 'tag.html', context={'tag': tag_request,
                                                 'questions': QUESTIONS,
                                                   'is_auth': IS_AUTH,
                                                   'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})


def questionList(request):
    shuffled_questions = random.sample(QUESTIONS, len(QUESTIONS))
    return render(request, 'questionList.html', context={
                                                        'questions': shuffled_questions,
                                                        'is_auth': IS_AUTH,
                                                        'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'question.html',  context={'questions': item,
                                                       'is_auth': IS_AUTH, 
                                                       'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS,
                                                        'ANSWERS': ANSWERS})

def ask(request):
    return render(request, 'ask.html', context= {'is_auth': IS_AUTH,
                                                  'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def login(request):
    return render(request, 'login.html', context= {'is_auth': IS_AUTH,
                                                    'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def register(request):
    return render(request, 'register.html', context= {'is_auth': IS_AUTH,
                                                       'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})


def settings(request):
    return render(request, 'settings.html', context= {'is_auth': IS_AUTH,
                                                      'is_auth': IS_AUTH,
                                                        'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def hot(request):
    shuffled_questions = random.sample(QUESTIONS, len(QUESTIONS))
    return render(request, 'hot.html', context={'questions': shuffled_questions,
                                                 'is_auth': IS_AUTH,
                                                   'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})
