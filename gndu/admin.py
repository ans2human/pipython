from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from gndu.models import Authors, Posts, Project


admin.site.register(Authors)


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_post', 'timestamp', 'link_to_user']
    
    def link_to_user(self, obj):

	    link = reverse("admin:auth_user_change", args=[obj.author_post])

	    return format_html('<a href="{}"> {}</a>', link, obj.author_post)

    link_to_user.short_description = 'UserID'



admin.site.register(Posts, PostsAdmin)
admin.site.register(Project)





# class Posts(models.Model):
#     title = models.CharField(max_length=50)
#     slug = models.SlugField(blank=True)
#     # date = timezone.now()
#     timestamp = models.DateTimeField(default=timezone.now)
#     body = models.TextField(max_length=500)
#     author_post = models.ForeignKey(Authors, on_delete=models.CASCADE)
#     objects = models.Manager()
#     def __str__(self):
#         return self.title
