from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('articles.urls'))
]