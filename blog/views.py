
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category, Comment
from .forms import ArticleForm, EditForm, CommentForm


def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('post_id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:article-detail', args=[str(pk)]))

def category(request, cats):
    category_by_post = Article.objects.filter(category=cats)
    context = {
        'category_by_post': category_by_post,
        'cats': cats,
    }
    return render(request, 'blog/category_page.html', context)


class ArticleView(ListView):

    model = Article
    template_name = 'blog/home.html'
    ordering = ['-date_creation',]


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/article_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stuff = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = stuff.total_like()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['now'] = timezone.now()
        context['total_likes'] = total_likes
        return context


class ArticleCreateView(CreateView):
    
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
 
    # fields = '__all__'



class ArticleCommentView(CreateView):
    
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('blog:home')




class ArticleUpdateView(UpdateView):
    
    model = Article
    form_class = EditForm
    template_name = 'blog/update_article.html'
    #fields = ['titre', 'slug', 'contenu']


class ArticleDeleteView(DeleteView):
    
    model = Article
    template_name = 'blog/delete_article.html'
    success_url = reverse_lazy('blog:home')


class AddCategoryView(CreateView):
    
    model = Category
    #form_class = ArticleForm
    template_name = 'blog/add_category.html'
    fields = '__all__'
