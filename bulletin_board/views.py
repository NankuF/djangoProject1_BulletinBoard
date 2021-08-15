from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import F, Case, Value, When

from .models import Bboard, Rubric, Client
from .forms import BboardForm
from .tasks import send_email_task

from django.views.decorators.cache import cache_page


@cache_page(120)
def bboard_index(request):
    """Главная страница со всеми рубриками"""
    bbs = Bboard.objects.all().select_related()
    rubrics = Rubric.objects.all().select_related()

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
    bbs = Bboard.objects.filter(rubric__slug=rubric_slug).select_related()
    rubrics = Rubric.objects.all().select_related()
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

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            send_email_task.delay()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def see_user_info(request):
    if settings.LOW_CACHE:
        key = 'user_info'
        user_info = cache.get(key)
        context = {
            key: user_info
        }
        if user_info is None:
            user_info = Bboard.objects.all().select_related()
            cache.set(key, user_info)
            context = {
                key: user_info
            }
    else:
        context = {
            'user_info': Bboard.objects.all().select_related()
        }
    # Берем объект с ценой 0 и меняем его на 1000
    if Bboard.objects.get(price=0):
        print(Bboard.objects.get(price=0))
        user_count = Bboard.objects.get(price=0)
        user_count.price = F('price') + 1000
        user_count.save()
    else:
        pass
    return render(request, 'bulletin_board/users_info.html', context)


def check_client_model():
    ann = Client.objects.annotate(
        discount=Case(
            When(account_type=Client.GOLD, then=Value('5%')),
            When(account_type=Client.PLATINUM, then=Value('10%'),
                 default=Value('0%'),
                 )
        )
    )
    return ann
       