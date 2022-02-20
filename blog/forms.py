
from django import forms
from .models import Article, Category, Comment

choices = Category.objects.all().values_list("name", "name")

choice_list = []
for item in choices:
    choice_list.append(item)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('titre', 'slug','author', 'category','contenu', 'status')

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=choice_list),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('titre', 'slug', 'author', 'category', 'contenu')

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=choice_list),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),   
        }
