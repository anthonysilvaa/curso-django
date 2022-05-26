from django.shortcuts import render
from django.urls import reverse

# Create your views here.
# Contexto do template

class Video:

    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse(('aperitivos:video'), args=(self.slug,))



videos = [
    Video('motivacao', 'Vídeo Solo Leveling', 713312782),
    Video('future-royalty', 'Vídeo Future Royalty', 713543859)
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
