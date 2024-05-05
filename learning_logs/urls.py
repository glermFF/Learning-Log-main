"""URL patterns"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # HomePage
    path('', views.index, name='index'),
    # Topics Page
    path('topics/', views.topics, name='topics'),
    # Detailed page for each topic
    path('topics/<str:topic_id>/', views.topic, name='topic'),
    # Adding a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]