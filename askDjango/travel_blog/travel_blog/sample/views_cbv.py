from django.http import HttpResponse
from django.views.generic import View, TemplateView


class PostListView1(View):
    def get(self, request):
        type = 'Class View HttpResponse Type'
        html = self.get_template_string().format(type=type)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1> CBV sample Page </h1>
            <p> {type} </p>
            <p>CBV HttpResponse Sample Page입니다.</p>'''

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'sample/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['type'] = 'CBV render Sample'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(object):
    pass


class ExcelDownloadView(object):
    pass
