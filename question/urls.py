from django.contrib import admin
from django.urls import path, include
from question import views

urlpatterns = [
    path('category/', views.category, name="category"),
    path('quiz/', views.question, name="question"),
    path('quiz2/', views.question2, name="question2"),
    path('quiz3/', views.question3, name="question3"),
    path('quiz4/', views.question4, name="question4"),
    path('quiz5/', views.question5, name="question5"),
    path('next/', views.next, name='next'),
    path('result/', views.result, name='result'),
    path("<int:category_id>/question_new/", views.question_new, name="question_new"),
    path("<int:question_id>/choice_new/", views.choice_new, name="choice_new"),
    path("<int:category_id>/question_new2/", views.question_new2, name="question_new2"),
    path("<int:question_id>/choice_new2/", views.choice_new2, name="choice_new2"),
    path("<int:category_id>/question_new3/", views.question_new3, name="question_new3"),
    path("<int:question_id>/choice_new3/", views.choice_new3, name="choice_new3"),
    path("<int:category_id>/question_new4/", views.question_new4, name="question_new4"),
    path("<int:question_id>/choice_new4/", views.choice_new4, name="choice_new4"),
    path("<int:category_id>/question_new5/", views.question_new5, name="question_new5"),
    path("<int:question_id>/choice_new5/", views.choice_new5, name="choice_new5"),
]