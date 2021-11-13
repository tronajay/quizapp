from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('quiz/<str:quiz>',views.quiz,name="quiz"),
    path('save-answer',views.saveans,name="saveans"),
    path('check-result',views.result,name="result"),
]
