from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from . models import Song

def index(request):
    songs = Song.objects.all()
    paginator = Paginator(songs, 8)
    page = request.GET.get('page')
    paged_songs = paginator.get_page(page)

    context = {
        'songs': paged_songs
    }
    return render(request, 'pages/index.html', context)

def search(request):
    query= request.GET.get('query')
    song= Song.objects.filter(description__icontains=query)
    context={
        'songs': song
    }

    return render(request, 'pages/search.html', context)


