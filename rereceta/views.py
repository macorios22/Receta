from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Receta, Categoria, Image, Integrante
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(login_required, name='dispatch')
class RecetaListView(LoginRequiredMixin,generic.ListView):
    model = Receta
    template_name = "list.html"

@method_decorator(login_required, name='dispatch')
class RecetaDetailView(LoginRequiredMixin,generic.DetailView):
    model = Receta
    template_name = "detail.html"

@method_decorator(login_required, name='dispatch')
class RecetaCreateView(LoginRequiredMixin,generic.CreateView):
    model = Receta
    fields = '__all__'
    template_name = "form.html"

@method_decorator(login_required, name='dispatch')
class RecetaUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Receta
    fields = '__all__'
    template_name = "form.html"

@method_decorator(login_required, name='dispatch')
class RecetaDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Receta
    template_name = "delete.html"
    success_url = reverse_lazy('rereceta:index')

@method_decorator(login_required, name='dispatch')
class CategoriaListView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    template_name = "categoria-list.html"

@method_decorator(login_required, name='dispatch')
class CategoriaDetailView(LoginRequiredMixin,generic.DetailView):
    model = Categoria
    template_name = "categoria-detail.html"

@method_decorator(login_required, name='dispatch')
class CategoriaCreateView(LoginRequiredMixin,CreateWithInlinesView):
    model = Categoria
    #inlines = [DetalleInLine]
    fields = '__all__'
    template_name = "categoria-form.html"

@method_decorator(login_required, name='dispatch')
class CategoriaUpdateView(LoginRequiredMixin,UpdateWithInlinesView):
    model = Categoria
    #inlines = [DetalleInLine]
    fields = '__all__'
    template_name = "categoria-form.html"

@method_decorator(login_required, name='dispatch')
class CategoriaDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Categoria
    template_name = "categoria-delete.html"
    success_url = reverse_lazy('rereceta:categoria-index')

@method_decorator(login_required, name='dispatch')
class ImagenCreateView(LoginRequiredMixin,generic.CreateView):
    model = Image
    fields = '__all__'
    template_name = "form-imagen.html"

@method_decorator(login_required, name='dispatch')
class IntegranteCreateView(LoginRequiredMixin,generic.CreateView):
    model = Integrante
    fields = '__all__'
    template_name = "form-integrante.html"
