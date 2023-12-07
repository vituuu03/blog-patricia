#Importação necessária
from django.contrib import admin
#Importação do modelo Post
from .models import Post
#Registro do modelo Post no site de administração
admin.site.register(Post)