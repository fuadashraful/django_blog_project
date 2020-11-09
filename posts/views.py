from django.shortcuts import render
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# POSTS VIEW ENDPOINT
def posts(request):
    context={}
    posts=requests.get('https://jsonplaceholder.typicode.com/posts').json()

    paginator=Paginator(posts,3)
    page = request.GET.get('page',1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        print("from here")
        posts = paginator.page(paginator.num_pages)

    context['posts']=posts
    return render(request, 'blog-listing.html',context)


# POST DETAILS VIEW ENDPOINT
def post_details(request,post_id): 
    api_text="https://jsonplaceholder.typicode.com/posts/"+str(post_id)
    post=requests.get(api_text).json()

    api_text="https://jsonplaceholder.typicode.com/posts/"+str(post_id)+"/comments"
    comments=requests.get(api_text).json()

    context={}
    context['post']=post
    context['comments']=comments
    return render(request, 'blog-post.html',context)