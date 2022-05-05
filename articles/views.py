from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Article, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView

# Create your views here.
def ArticlesView(request):
    articles ={'articles' : Article.objects.all()} 
    return render(request, template_name="articles.html", context=articles)

def ArticleCommentView(request, pk):
    article = Article.objects.get(id = pk)
    comments = Comment.objects.filter(article=article)
    context = {'comments':comments, 'article':article}
    return render(request, template_name='article_comments.html', context=context)


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "create_article.html"
    fields = ['title', 'body']
    login_url='login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = 'article'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = ['title', 'body']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user