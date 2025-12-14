from django.urls import path

from . import views

urlpatterns = [
    # path('', ),
    path('posts/', views.get_post_list),
]