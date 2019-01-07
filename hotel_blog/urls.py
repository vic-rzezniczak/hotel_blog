from django.urls import path

from . import views

urlpatterns = [    
    path('', views.index, name='index'), # ex: /hotel_blog/
    path('<int:question_id>/', views.detail, name='detail'), # ex: /hotel_blog/5/
    path('<int:question_id>/results/', views.results, name='results'), # ex: /hotel_blog/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /hotel_blog/5/vote/
    ]