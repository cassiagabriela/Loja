from django.contrib import messages
from django.shortcuts import render, redirect,reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from .models import Produto
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, View, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class DetalhesView(DetailView):
    login_url = 'login'
    model = Produto
    template_name = 'detalhe.html'
    context_object_name = 'produtos'


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


    def post(self, request, *args, **kwargs):
        username = request.POST.get('user')
        password = request.POST.get('senha')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario e senha inválidos, tente novamente')
            return redirect('login')


class ListaProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'


class CriaProdutoView(CreateView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'cadastrar_produtos.html'
    fields = ['titulo','descricao','preco','referencia','imagem','quantidade','categoria', 'promocao','precopromocao','user']

    def get_success_url(self):
        return reverse('index')


class DeleteProdutoView(LoginRequiredMixin, DeleteView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'confirma_delete.html'

    def get_success_url(self):
        return reverse('index')


class AtualizarProdutoView(LoginRequiredMixin, UpdateView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'editar_produtos.html'
    fields = ['titulo','descricao','preco']


    def get_success_url(self):
        return reverse('index')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
      logout(request)
      return redirect('/login')


class FilterPromocaoView(View):
    def get(self, request, *args, **kwargs):
      promo = Produto.objects.filter(promocao=True)
      return render(request, 'produtos.html', {'produtos': promo})


class FilterCategoriasView(View):
    def get(self, request, *args, **kwargs):
        context = super(FilterCategoriasView, self).get_context_data(**kwargs)
        prod = Produto.objects.filter(categoria=context)
        return render(request, 'produtos.html', {'produtos': prod})


class FilterMyProductsView(View):
    def get(self, request, *args, **kwargs):
        prod = Produto.objects.filter(user=request.user)
        return render(request, 'produtos.html', {'produtos': prod})


class RegistroView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registrar_usuario.html')

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        password = request.POST.get('senha')
        email = request.POST.get('email')
        User.objects.create(username=username, password=password, email=email, first_name=nome)
        return redirect('login')