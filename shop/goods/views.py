from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView
from .models import Product
from .utils import q_search


class ProductView(DetailView):
    model = Product
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["object"].name
        return context


class CatalogView(ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "products"
    paginate_by = 8
    slug_url_kwarg = "category_slug"

    def get_queryset(self) -> QuerySet[Any]:
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get("on_sale")
        search_query = self.request.GET.get("search_query")
        order_by = self.request.GET.get("order_by")

        if category_slug == 'all':
            goods = super().get_queryset()
        elif search_query:
            goods = q_search(search_query)
        else:
            goods = super().get_queryset().filter(cat__slug=category_slug) 

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by:
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["products"]:
            cat = context["products"][0].cat
            context["title"] = "Категория " + cat.name
            context['slug_url'] = self.kwargs.get(self.slug_url_kwarg)
            return context
        context["title"] = "Категория"
        context['slug_url'] = self.kwargs.get(self.slug_url_kwarg)
        return context
