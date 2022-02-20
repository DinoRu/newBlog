from django.urls import path, include
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='home'),
    path('article_detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article_create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article/edit/<int:pk>/', views.ArticleUpdateView.as_view(), name='article-edit'),
    #path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('article/<int:pk>/remove', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('category/<str:cats>/', views.category, name='category'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('article/<int:pk>/comment/', views.ArticleCommentView.as_view(), name='article-comment'),

]