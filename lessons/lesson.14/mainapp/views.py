from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Category, Animal
from .forms import AnimalForm, ContactForm


def index_view(request):
    return render(request, 'mainapp/index.html')


def category_list_view(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'mainapp/category_list.html', context=context)


class CategoryListView(ListView):
    model = Category
    ordering = ['pk']
    # template_name = ''
    # context_object_name =

    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # get_queryset - получение данных

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['some_text'] = 'Another text'
        return context



class CategoryDetailView(DetailView):
    model = Category

    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # get_queryset - получение данных
    # get_object - получение одного объекта


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('mainapp:category_list')

    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # post
    # form_valid
    # get_success_url

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('mainapp:category_list')

    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # post
    # form_valid
    # get_object
    # get_success_url

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('mainapp:category_list')
    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # post
    # form_valid
    # get_object
    # get_success_url


class AnimalListView(ListView):
    model = Animal
    template_name = 'mainapp/animals.html'

    def get(self, request, *args, **kwargs):
        self.category_id = request.GET.get('category_id', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.category_id is not None:
            queryset = queryset.filter(category__id=self.category_id)

        queryset = queryset.select_related('category')
        queryset = queryset.prefetch_related('food')
        return queryset


class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('mainapp:animal_list')


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('mainapp:index')
    template_name = 'mainapp/contact.html'

    def form_valid(self, form):
        data = form.cleaned_data
        print('MESSAGE', data['message'])
        return super().form_valid(form)
