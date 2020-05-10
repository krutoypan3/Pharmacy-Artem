from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import models

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=models.Articles.objects.all().order_by("title")[:20],
                             template_name="lekarstva/posts.html")),
    url('(?P<pk>\d+)', DetailView.as_view(model=models.Articles, template_name="lekarstva/post.html"))
]
