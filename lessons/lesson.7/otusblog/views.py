from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView


# def index_view(request):
#     if request.method == 'POST':
#         pass
#         return render(...)
#     # return HttpResponse('<h1>Hello world!</h1>')
#     return render(request, 'otusblog/index.html')


# class IndexPageView(View):
#     template_name = 'otusblog/index.html'
#
#     def get(self, request):
#         args = {
#             'spam': 'eggs',
#             'foo': 'bar',
#         }
#         return render(request, self.template_name, context=args)


class IndexPageView(TemplateView):
    template_name = 'otusblog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'spam': 'eggs',
            'foo': 'bar',
        })
        return context
