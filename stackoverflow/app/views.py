from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.db.models import Count

TAG_TOP_TITLES = models.Tag.objects.get_top_five_tags().values_list('title', flat=True)

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

def question_list(request):
    all_questions = models.Question.objects.all()
    page_items = paginate(all_questions, request, per_page=30)


    return render(request, 'question_list.html', context={
        'questions': page_items,
        'is_auth': True,
        'POPULAR_TAGS': TAG_TOP_TITLES
    })

def hot(request):
    hot_questions = models.Question.objects.sort_by_answers_count()
    page_items = paginate(hot_questions, request, per_page=30)

    return render(request, 'hot.html', context={'questions': page_items,
                                                 'is_auth': False,
                                                   'POPULAR_TAGS': TAG_TOP_TITLES})

def ask(request):
    return render(request, 'ask.html', context= {'is_auth': False,
                                                 'POPULAR_TAGS': TAG_TOP_TITLES})

def login(request):
    return render(request, 'login.html', context= {'is_auth': False,
                                                   'POPULAR_TAGS': TAG_TOP_TITLES})

def register(request):
    return render(request, 'register.html', context= {'is_auth': False,
                                                       'POPULAR_TAGS': TAG_TOP_TITLES})

def settings(request):
    return render(request, 'settings.html', context= {'is_auth': True,
                                                      'POPULAR_TAGS': TAG_TOP_TITLES})

def question(request, question_id):
    question_item = get_object_or_404(models.Question, id=question_id)
    
    answers = models.Answer.objects.filter(question=question_item)
    tegs_in_question = question_item.tags.all()
    page_items = paginate(answers, request, per_page=10)
    return render(request, 'question_item.html', context={'question': question_item,
                                                          'ANSWERS': page_items,
                                                          'is_auth': False, 
                                                          'POPULAR_TAGS': TAG_TOP_TITLES,
                                                          'ANSWER_TEGS': tegs_in_question})

def tag(request, tag_name):
    page_items = paginate(models.Question.objects.get_by_tag(tag_name), request, per_page=20)
    return render(request, 'tag.html', context={'tag': tag_name,
                                                 'questions': page_items,
                                                   'is_auth': True,
                                                   'POPULAR_TAGS': TAG_TOP_TITLES})



