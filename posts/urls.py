from django.urls import path
from . import views
from .views import PostListView , PostCreateView , PostUpdateView , PostDeleteView , detalhe_post

urlpatterns = [
    path('lista/', views.lista_posts, name='lista_posts'),
    path('cbv-lista/', PostListView.as_view(), name='cbv_lista_posts'),
    path('novo/', PostCreateView.as_view(), name='novo_post'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('posts/<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('posts/<int:pk>/detalhe/', detalhe_post, name='detalhe_post'),
]

## Arthur Américo Marques

