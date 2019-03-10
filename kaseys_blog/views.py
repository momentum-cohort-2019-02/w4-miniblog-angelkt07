import datetime

from django.shortcuts import render
from kaseys_blog.models import BlogPost, Blogger, BlogComment, Topic
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    """View function for home page of site"""

    num_blogpost = BlogPost.objects.all().count()
    num_comments = BlogComment.objects.all().count()
    num_blogger = Blogger.objects.count()
    num_topic = Topic.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogpost' : num_blogpost,
        'num_blogger' : num_blogger,
        'num_topic' : num_topic,
        'num_visits' : num_visits,
    }

    return render(request, 'index.html', context=context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

class TopicDetailView(generic.DetailView):
    model = Topic

class TopicListView(generic.ListView):
    model = Topic


# Going to make it to where a Blogger can see all of their BlogPosts
class BlogPostByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BlogPost
    paginate_by = 5

    def queryset(self):
        pass

# Going to make to where a Blog Administrator can view all blogs
class BlogPostByAllUserListView(LoginRequiredMixin,generic.ListView):
    model = BlogPost
    paginate_by = 5

    def get_queryset(self):
        pass

class BloggerCreate(CreateView):
    model = Blogger
    fields = '__all__'

class BloggerUpdate(UpdateView):
    model = Blogger
    fields = ['first_name', 'last_name', 'occupation', 'city']

class BloggerDelete(DeleteView):
    model = Blogger
    success_url = reverse_lazy('bloggers')

class BlogPostCreate(CreateView):
    model = BlogPost
    fields = '__all__'

class TopicCreate(CreateView):
    model = Topic
    fields = '__all__'

class BlogCommentCreate(CreateView):
    model = BlogComment
    fields = '__all__'
    initial = {'comment_date' : comment_date}

