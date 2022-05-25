from django.shortcuts import render

# Create your views here.

#Contexto do template
def video(request, slug):

    videos = {

       'motivacao':{'titulo': 'Vídeo SoloLeveling', 'vimeo_id': 713312782},
        'future-royalty': {'titulo': 'Vídeo Future Royalty', 'vimeo_id': 713543859}

    }

    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
