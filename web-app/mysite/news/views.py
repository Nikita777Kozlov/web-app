from django.shortcuts import render,redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView,UpdateView,DeleteView


class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

# Create your views here.
class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/detail_view.html'
    context_object_name = 'artile'

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news'
    template_name = 'news/news-delete.html'


def news_home(request):
    news = Artiles.objects.order_by('date')
    return render(request, 'news/news_home.html',{'news':news})


def create(request):
    error = ''
    if request.method =='POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error ='Форма была неверной'
    form =ArtilesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request,'news/create.html',data)