from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Post
from datetime import datetime

# def homepage(request):
#     posts=Post.objects.all()
#     print(posts)
#     post_list=[]
#
#     for count ,post in enumerate(posts):
#         print(count)
#         post_list.append("No.{}".format(str(count))+"<hr>")
#
#         post_list.append("<small>"+str(post.body)\
#                          +"</small><br><br>")
#     return HttpResponse(post_list)

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    print(slug)
    #try:
    post = Post.objects.get(slug=slug)
    print(post)
    if post!=None:
        return render(request,'post.html',locals())
    #except:
    #    return redirect('/test/')

def test(request):
    return HttpResponse('test')