from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    galochka = Articles.objects.first()
    return render(request,'news/news_home.html', {"news":news, "NewsHide":galochka})


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = "news/create.html"

    form_class = ArticlesForm

class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"


def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    form = ArticlesForm()

    data =  {
        'form':form
    }


    return render(request,'news/create.html', data)