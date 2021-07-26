from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Bboard, Rubric
from .forms import BboardForm


def bboard_index(request):
    """Главная страница со всеми рубриками"""
    bbs = Bboard.objects.all()
    rubrics = Rubric.objects.all()

    context = {
        'title': 'Главная',
        'bbs': bbs,
        'rubrics': rubrics,
    }

    return render(request, 'bulletin_board/index.html', context)


def by_rubric(request, rubric_pk):
    """Отдельно выбранная рубрика"""
    current_rubric = Rubric.objects.get(pk=rubric_pk)
    bbs = Bboard.objects.filter(rubric=rubric_pk)
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'bulletin_board/by_rubric.html', context)


def contacts(request):
    """Страница контактов"""
    context = {'title': 'Контакты'}
    return render(request, 'bulletin_board/contacts.html', context)


class BbCreateView(CreateView):
    """Страница добавления объявления с привязкой к юзеру"""
    template_name = 'bulletin_board/create.html'
    form_class = BboardForm
    success_url = reverse_lazy('bboard:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BbCreateView, self).form_valid(form)
