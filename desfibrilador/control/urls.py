from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
	       path('<int:id_desfibrilador>/', views.detail, name='detail'),
	       path('<int:id_desfibrilador>/results/', views.results, name='results'),
               path('login', views.login, name='login'),
              ]
