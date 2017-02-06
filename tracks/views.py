from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Track


def track_view(request, title):
    template = 'track.html'
    track = get_object_or_404(Track, title=title)
    bio = track.artist.biography

    context = {
        'track': track,
        'bio': bio,
    }
    return render(request, template, context)
