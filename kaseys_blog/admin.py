from django.contrib import admin
from kaseys_blog.models import Topic, BlogPost, BlogComment, Blogger

# Register your models here.

admin.site.register(Topic)

# Define the admin Blogger class
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'occupation', 'city', 'email')
    fields = ['first_name', 'last_name', ('occupation', 'city')]

admin.site.register(Blogger, BloggerAdmin)
class BlogCommentInLine(admin.TabularInline):
    model = BlogComment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'display_topic')
    inlines = [BlogCommentInLine]


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blogpost',)
    fieldsets = (
        (None, {
            'fields': ('blogpost', 'comment', 'id')
        }),
    )


