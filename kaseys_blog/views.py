from django.shortcuts import render
from django.views import generic
from kaseys_blog.models import BlogPost, Blogger, BlogComment, Topic

def index(request):
    """View function for home page of site"""

    num_blogpost = BlogPost.objects.all().count()
    num_comments = BlogComment.objects.all().count()
    num_blogger = Blogger.objects.count()

    context = {
        'num_blogpost' : num_blogpost,
        'num_comments' : num_comments,
        'num_blogger' : num_blogger,
    }

    return render(request, 'index.html', context=context)

class BlogPostListView(generic.ListView):
    model = BlogPost

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
