from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
# from .models import Person
from mainapp.models import Person


class IndexView(ListView):
    model = Person


def person_detail_view(request):
    id = request.GET.get('id')
    if id is None:
        raise Http404

    person = get_object_or_404(Person, id=id)
    return render(request, 'mainapp/person_detail.html', {'object': person})


@method_decorator(csrf_exempt, name='dispatch')
class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url = '/'
