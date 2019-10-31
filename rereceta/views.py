from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Receta, Categoria,Image
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


class RecetaListView(generic.ListView):
    model = Receta
    template_name = "list.html"


class RecetaDetailView(generic.DetailView):
    model = Receta
    template_name = "detail.html"


class RecetaCreateView(generic.CreateView):
    model = Receta
    fields = '__all__'
    template_name = "form.html"


class RecetaUpdateView(generic.UpdateView):
    model = Receta
    fields = '__all__'
    template_name = "form.html"


class RecetaDeleteView(generic.DeleteView):
    model = Receta
    template_name = "delete.html"
    success_url = reverse_lazy('rereceta:index')


class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = "categoria-list.html"


class CategoriaDetailView(generic.DetailView):
    model = Categoria
    template_name = "categoria-detail.html"


class CategoriaCreateView(CreateWithInlinesView):
    model = Categoria
    #inlines = [DetalleInLine]
    fields = '__all__'
    template_name = "categoria-form.html"


class CategoriaUpdateView(UpdateWithInlinesView):
    model = Categoria
    #inlines = [DetalleInLine]
    fields = '__all__'
    template_name = "categoria-form.html"


class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    template_name = "categoria-delete.html"
    success_url = reverse_lazy('rereceta:categoria-index')
