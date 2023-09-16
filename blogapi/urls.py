from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.index),
    path('get-all-post/',views.get_all_post),
    path('create-post/',views.create_post),
    path('delete-post/<int:id>',views.delete_post),
    path('get-post/<int:id>',views.get_post),
    path('update-post/<int:id>',views.update_post),
]