from django.contrib import messages
from django.shortcuts import render, redirect,reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from .models import Produto
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


def registrar(request):
    if request.POST:
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        password = request.POST.get('senha')
        email = request.POST.get('email')
        User.objects.create(username=username, password=password, email=email, first_name=nome)

    return redirect('login')


def set_cadastro(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    referencia = request.POST.get('referencia')
    preco = request.POST.get('preco')
    imagem = request.FILES['imagem']
    quantidade = request.POST.get('quantidade')
    categoria = request.POST.get('categoria')
    promocao = request.POST.get('promocao')
    precopromocao = request.POST.get('precopromocao')
    user = request.user
    produto = Produto.objects.create(titulo=titulo, descricao=descricao, referencia=referencia, preco=preco, imagem=imagem,
                                     quantidade=quantidade, categoria=categoria, promocao=promocao, precopromocao=precopromocao, user=user)
    url = 'detalhe/{}/'.format(produto.id)
    return redirect(url)


def delete_produto(request, id):
    prod = Produto.objects.get(id=id)
    if prod.user == request.user:
        prod.delete()
    return redirect('/')




class AtualizarProdutoView(UpdateView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'editar_produtos.html'
    fields = ['titulo','descricao','preco']


    def get_success_url(self):
        return reverse('index')





# class CadastrarProdutoView(View):
#
#     def get(self, request, *args, **kwargs):
#         context = {}
#         produto = get_object_or_404(Produto, id=)
#         context['produto'] = produto
#         if produto.user == request.user:
#             return render(request, 'editar_produtos.html', context)
#
#
#     def post(self, request, *args, **kwargs):
#         produto = Produto.objects.get(id=id)
#         titulo = request.POST.get('titulo')
#         descricao = request.POST.get('descricao')
#         referencia = request.POST.get('referencia')
#         preco = request.POST.get('preco')
#         imagem = request.FILES.get('imagem')
#         quantidade = request.POST.get('quantidade')
#         categoria = request.POST.get('categoria')
#         promocao = request.POST.get('promocao')
#         precopromocao = request.POST.get('precopromocao')
#
#         if produto.user == request.user:
#             produto.titulo = titulo
#             produto.preco = preco
#             produto.descricao = descricao
#             produto.referencia = referencia
#             produto.quantidade = quantidade
#             produto.categoria = categoria
#             produto.promocao = promocao
#             produto.precopromocao = precopromocao
#             if imagem:
#                 produto.imagem = imagem
#             produto.save()
#             url = f'/detalhe/{produto.id}/'
#             return redirect(url)
#         return redirect('/')

def edite_produto(request, id):
    context = {}
    produto = get_object_or_404(Produto, pk=id)
    context['produto']=produto
    if produto.user == request.user:
      return render(request, 'editar_produtos.html',context)
    return redirect('/')


def editar_submit(request, id):

    produto = Produto.objects.get(id=id)
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    referencia = request.POST.get('referencia')
    preco = request.POST.get('preco')
    imagem = request.FILES.get('imagem')
    quantidade = request.POST.get('quantidade')
    categoria = request.POST.get('categoria')
    promocao = request.POST.get('promocao')
    precopromocao = request.POST.get('precopromocao')

    if produto.user == request.user:
        produto.titulo = titulo
        produto.preco = preco
        produto.descricao = descricao
        produto.referencia = referencia
        produto.quantidade = quantidade
        produto.categoria = categoria
        produto.promocao = promocao
        produto.precopromocao = precopromocao
        if imagem:
            produto.imagem = imagem
        produto.save()
        url = f'/detalhe/{produto.id}/'
        return redirect(url)
    return redirect('/')

def cadastro_produto(request):
    return render(request, 'cadastrar_produtos.html')


def registro(request):
    return render(request, 'registrar_usuario.html')


def logout_user(request):
    logout(request)
    return redirect('/login')


def lista(request):
    prod = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': prod})


class ListaProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'


def promocao(request):
    promo = Produto.objects.filter(promocao=True)
    return render(request, 'produtos.html', {'produtos': promo})


def categorias(request, categoria):
    prod = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos.html', {'produtos': prod})


def index(request):
    return render(request, 'index.html')



class DetalhesView(LoginRequiredMixin, DetailView):
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


