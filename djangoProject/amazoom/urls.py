from django.urls import path

from . import views

urlpatterns = [
    # ex: /amazoom/
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.user_register, name='signup'),
    path('add_item/', views.ItemAdd.as_view(), name='additem'),
]