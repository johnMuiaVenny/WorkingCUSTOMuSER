from django.urls import path
from .views import *
from . import views


app_name = 'COMMENTS'

urlpatterns = [
    path('', allComments.as_view(), name='allComments'),
    path('<int:pk>/Comment', Comment.as_view(), name = 'Comment'),
    path('AddComment', AddComment.as_view(), name = 'AddComment'),
    path('<int:pk>', UpdateComment.as_view(), name = 'UpdateComment'),
    path('<int:pk>/delete', DeleteComment.as_view(), name = 'DeleteComment'),
]