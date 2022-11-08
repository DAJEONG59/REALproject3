from django.urls import path
from diary import views

urlpatterns = [
    path("", views.memory_list),
    path("<int:pk>/", views.memory_detail),
    path("new/", views.memory_new),
    path("<int:pk>/edit/", views.memory_edit),
    path("<int:pk>/delete/", views.memory_delete),
    path("gallery/", views.gallery),


    path("keyword/new/", views.keyword_new),
    path("keyword/<int:pk>/", views.k_detail_page),
    path("keyword/<int:pk>/edit/", views.key_edit),
    path("keyword/<int:pk>/delete/", views.key_delete),



]
