from django.shortcuts import render
# from django.http import HttpResponse

from blog.models import Post

# def home_view(requst):
#     return HttpResponse("Главная страница")

def get_post_list(request):
    posts = Post.objects.all()

    return render(request=request, template_name='blog/post_list.html',context={'posts': posts})
