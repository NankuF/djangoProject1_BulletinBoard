from django.shortcuts import render


def bboard_index(request):
    context = {'title': 'Главная'}
    return render(request, 'bulletin_board/index.html', context)


def contacts(request):
    context = {'title': 'Контакты'}
    return render(request, 'bulletin_board/contacts.html', context)
