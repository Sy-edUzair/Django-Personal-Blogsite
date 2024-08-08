from django.urls import path
from . import views


urlpatterns = [
    path("",views.HomePageView.as_view(),name = "home-page"),
    path("posts",views.AllPostsView.as_view(),name="posts-page"),
    path("posts/<slug:slug>",views.SinglePostView.as_view() ,name="posts-details-page"),
    #slug: is a transformer matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.
    #posts/my-first-post(this is called a slug)(it is SEO friendly)
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
