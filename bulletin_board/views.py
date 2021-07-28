from django.shortcuts import render, get_object_or_404
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


def by_rubric(request, rubric_slug):
    """Отдельно выбранная рубрика"""
    current_rubric = Rubric.objects.get(slug=rubric_slug)
    # или так, тоже работает
    # current_rubric = get_object_or_404(Rubric, slug=rubric_slug)
    bbs = Bboard.objects.filter(rubric__slug=rubric_slug)
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
