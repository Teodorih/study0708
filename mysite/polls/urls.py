from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('question/', views.IndexView.as_view(), name='index'),
    path('question/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('question/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('question/create/', views.QuestionCreate.as_view(), name='create'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='update'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='delete')
]
