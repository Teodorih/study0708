from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create/', views.QuestionCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.QuestionUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.QuestionDelete.as_view(), name='delete')
]
