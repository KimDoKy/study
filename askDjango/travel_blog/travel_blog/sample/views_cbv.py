from django.http import HttpResponse
from django.views.generic import View


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

class PostListView2(object):
    pass


class PostListView3(object):
    pass


class ExcelDownloadView(object):
    pass
