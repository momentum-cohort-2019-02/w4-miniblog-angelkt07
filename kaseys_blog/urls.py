from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogposts/', views.BlogPostListView.as_view(), name='blogposts'),
    path('blogpost/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('topics/', views.TopicListView.as_view(), name='topics'),
    # path('myblogposts/', views.BlogPostByUserListView.as_view(), name='my-blogposts'),
    # path('allblogposts/', views.BlogPostByAllUsersListView.as_view(), name='all-blogposts'),
    path('blogger/create/', views.BloggerCreate.as_view(), name='blogger_create'),
    path('blogger/<int:pk>/update/', views.BloggerUpdate.as_view(), name='blogger_update'),
    path('blogger/<int:pk>/delete/', views.BloggerDelete.as_view(), name='blogger_delete'),
    path('blogpost/create/', views.BlogPostCreate.as_view(), name='blogpost_create'),
    path('topic/create/', views.TopicCreate.as_view(), name='topic_create'),
]