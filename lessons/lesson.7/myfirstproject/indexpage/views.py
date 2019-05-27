from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView


# def index_page(request):
#     # return HttpResponse('<h1>Hello index!</h1>')
#     return render(request, 'indexpage/index.html')


# class IndexPageView(View):
#     template_name = 'indexpage/index.html'
#
#     def get(self, request):
#         # logic
#         args = {
#             'spam': 'eggs',
#             'foo': 'bar',
#         }
#         return render(request, self.template_name, args)

class IndexPageView(TemplateView):
    template_name = 'indexpage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'spam': 'eggs',
            'foo': 'bar',
        })
        return context

    def post(self, request):
        return HttpResponse('OK')
