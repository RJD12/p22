from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Proyecto, Categoria,Image,Integrante
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


class ProductoListView(generic.ListView):
    model = Proyecto
    template_name = "list.html"


class ProductoDetailView(generic.DetailView):
    model = Proyecto
    template_name = "detail.html"


class ProductoCreateView(generic.CreateView):
    model = Proyecto
    fields = '__all__'
    template_name = "form.html"


class ProductoUpdateView(generic.UpdateView):
    model = Proyecto
    fields = '__all__'
    template_name = "form.html"


class ProductoDeleteView(generic.DeleteView):
    model = Proyecto
    template_name = "delete.html"
    success_url = reverse_lazy('tienda:index')


class FacturaListView(generic.ListView):
    model = Categoria
    template_name = "facturas-list.html"


class FacturaDetailView(generic.DetailView):
    model = Categoria
    template_name = "facturas-detail.html"

    # def get_context_data(self, **kwargs):
    #   context = super(FacturaDetailView, self).get_context_data(**kwargs)
    #  context["detalle"] = Detalle.objects.filter(factura=self.object)
    # return context


# class DetalleInLine(InlineFormSetFactory):
 #   model = Detalle
  #  fields = '__all__'

class FacturaCreateView(CreateWithInlinesView):
    model = Categoria
    #inlines = [DetalleInLine]
    fields = '__all__'
    template_name = "facturas-form.html"


class FacturaUpdateView(UpdateWithInlinesView):
    model = Categoria
    #inlines = [DetalleInLine]
    fields = '__all__'
    template_name = "facturas-form.html"


class FacturaDeleteView(generic.DeleteView):
    model = Categoria
    template_name = "facturas-delete.html"
    success_url = reverse_lazy('tienda:factura-index')

class ImagenCreateView(generic.CreateView):
    model = Image
    fields = '__all__'
    template_name = "form-imagen.html"

class IntegranteCreateView(generic.CreateView):
    model = Integrante
    fields = '__all__'
    template_name = "form-integrante.html"