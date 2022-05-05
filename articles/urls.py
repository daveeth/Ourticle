from django.urls import path
from .views import ( ArticlesView, 
                    ArticleCommentView,
                    ArticleCreateView, 
                    ArticleDetailView, 
                    ArticleUpdateView, 
                    ArticleDeleteView)

urlpatterns = [
    path('', ArticlesView, name='home'),
    path('article/new', ArticleCreateView.as_view(), name='create_article'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/comment/<int:pk>', ArticleCommentView, name='comments')
]