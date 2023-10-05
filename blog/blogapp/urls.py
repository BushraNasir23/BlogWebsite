from django.urls import path

from . import views

urlpatterns=[
    path('',views.frontpage,name="frontpage"),
    path('about/',views.aboutpage,name="about"),
    path('detail/<slug:category_slug>/<slug:slug>/',views.detail,name="detail"),
    path('category<slug:slug>',views.category,name="category"),
    path('search',views.search,name="search"),
]