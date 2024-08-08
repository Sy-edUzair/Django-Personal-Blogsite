from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm

# Create your views here.

class HomePageView(ListView):
    template_name = "blog/home.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "lposts" #default is "object_list"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
    
class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def is_stored_post(self,request,post_slug):
        stored_posts = request.session.get("stored-posts")
        
        if stored_posts is not None:
            saved_for_later = post_slug in stored_posts
        else:
            saved_for_later=False
        return saved_for_later
    
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        return render(request,"blog/posts-details.html",{
            "identified_post": post,
            "post_tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "saved_for_later":self.is_stored_post(request,post.slug)
        })


    def post(self,request,slug):
        comment_form=CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            #commit is used to not let it hit DB and that we can edit a new model instance and then save it
            comment.post = post 
            comment.save()
            return HttpResponseRedirect(reverse("posts-details-page",args=[slug]))
        
        else:
            return render(request,"blog/posts-details.html",{
                "identified_post": post,
                "post_tags":post.tags.all(),
                "comment_form":comment_form,
                "comments":post.comments.all().order_by("-id"),
                "saved_for_later":self.is_stored_post(request,post.slug)
            })



#this will do all the things of "posts_detail_view"


class ReadLaterView(View):
    def post(self,request):
        storedposts=request.session.get("stored-posts")

        if storedposts is None:
            storedposts=[]
        postslug = request.POST["post_slug"]
        print(postslug)
        if postslug not in storedposts:#no duplicate ids check
            storedposts.append(postslug)
        else:#if it is in read later list then do this
            storedposts.remove(postslug)

        request.session["stored-posts"] = storedposts
        return HttpResponseRedirect(reverse("posts-details-page",args=[postslug]))
    
    def get(self,request):
        storedposts=request.session.get("stored-posts")

        context = {}
        if storedposts is None or len(storedposts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Post.objects.filter(slug__in=storedposts) #the "__in" modifier mean that I want slugs that are stored in storedposts list only
            context["has_posts"] = True

        return render(request,"blog/stored-posts.html",context)

        

        
'''
def homepage(request):
    latest_posts=Post.objects.all().order_by("-date")[:3] #display 3 latest posts(this is optimized command since Django will convert this whole command into a SQL query)(Django doesnt support negative indexing hence we do it "-date" instead of "date" which means order it in descending and then use slicing to fetch three latests posts)
    return render(request, "blog/home.html",{
        "lposts": latest_posts
    })
'''
"""def posts_view(request):
    posts = Post.objects.all().order_by("-date")
    return render(request,"blog/all_posts.html",{
        "all_posts":posts
    })
"""
"""def post_details(request, slug ):
    #identified_post = Post.objects.get(slug=Slug)
    identified_post = get_object_or_404(Post,slug=  slug)
    return render(request,"blog/posts-details.html",{
        "identified_post":identified_post,
        "post_tags":identified_post.tags.all()
    })
"""