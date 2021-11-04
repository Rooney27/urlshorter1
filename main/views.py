from django.shortcuts import render, redirect
import random
import string
from .forms import Url
from .models import UrlData


def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for x in
                           range(6))
            url = form.cleaned_data['url']
            new_url = UrlData(url=url, slug=slug,
                              user=request.user.username)
            new_url.save()

            context = {
                'form': form,
                'url': 'https//' + str(request.META['HTTP_HOST']) + '/' \
                    + str(slug),
                'domain': 'https//' + str(request.META['HTTP_HOST']),
                'slug': slug,
                }
            return render(request, 'index.html', context)
    else:
        form = Url()
        context = {'form': form}
    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)


def urlsHistory(request):
    urls_history = UrlData.objects.filter(user=request.user.username)
    context = {'urls_history': urls_history}
    return render(request, 'history.html', context)
