from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)

from .models import Category


class ShopAppIndexView(TemplateView):
    template_name = "shop_app/index.html"


class CategoriesListView(ListView):
    # model = Category
    queryset = Category.objects.filter(archived=False).order_by("id").all()


class CategoryDetailView(DetailView):
    model = Category
    # queryset = Category.objects.filter(archived=False).order_by("id").all()


class CategoryCreateView(CreateView):
    model = Category
    fields = "name", "description"
    # success_url = reverse_lazy("shop_app:categories")

    def get_success_url(self):
        return reverse("shop_app:category", kwargs={"pk": self.object.pk})


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("shop_app:categories")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return redirect(success_url)
