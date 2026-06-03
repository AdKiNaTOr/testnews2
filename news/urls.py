from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = (
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
)



