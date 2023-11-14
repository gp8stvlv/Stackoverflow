import random
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

IS_AUTH = True

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

QUESTIONS = [
    {
        'id': i,
        'title': f'question number {i}',
        'body': f'this is a very very long question... that has {i} id',
        'tags': ['new tag', 'python'],
        'answer_count': 1,
        'like_count': 2
    } for i in range(50)
]

def tag(request, tag_name):
    tag_request = None
    for tag in TAGS:
        if tag['name'] == tag_name:
            tag_request = tag
            break

    tagged_questions = [question for question in QUESTIONS if tag_name in question['tags']]
    page_items = paginate(tagged_questions, request, per_page=4)

    return render(request, 'tag.html', context={'tag': tag_request,
                                                 'questions': page_items,
                                                   'is_auth': True,
                                                   'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def paginate(objects, request, per_page=3):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(objects, per_page)

    try:
        page_items = paginator.page(current_page)
    except PageNotAnInteger:
        page_items = paginator.page(1)
    except EmptyPage:
        page_items = paginator.page(paginator.num_pages)

    return page_items


def questionList(request):
    all_questions = QUESTIONS
    page_items = paginate(all_questions, request, per_page=5)

    return render(request, 'questionList.html', context={
        'questions': page_items,
        'is_auth': True,
        'POPULAR_TAGS': POPULAR_TAGS,
        'BEST_MEMBERS': BEST_MEMBERS
    })



def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'question.html',  context={'questions': item,
                                                       'is_auth': False, 
                                                       'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS,
                                                        'ANSWERS': ANSWERS})

def ask(request):
    return render(request, 'ask.html', context= {'is_auth': False,
                                                  'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def login(request):
    return render(request, 'login.html', context= {'is_auth': False,
                                                    'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def register(request):
    return render(request, 'register.html', context= {'is_auth': False,
                                                       'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def settings(request):
    return render(request, 'settings.html', context= {'is_auth': True,
                                                        'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})

def hot(request):
    all_questions = QUESTIONS
    page_items = paginate(all_questions, request, per_page=5)
    return render(request, 'hot.html', context={'questions': all_questions,
                                                 'is_auth': False,
                                                   'POPULAR_TAGS': POPULAR_TAGS,
                                                        'BEST_MEMBERS': BEST_MEMBERS})
