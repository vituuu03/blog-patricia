#Importação necessária
from django.shortcuts import render
#Importação do modelo Post
from blog.models import Post
#Função que renderiza a página inicial
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

#Função que renderiza a página de um post
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post': post})

