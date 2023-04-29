from django.views.generic import DetailView

From App_List.models import booklist

class booklist(DetailView):
    model= booklist
    template_name='App_List/booklist.html'
