import pytest
from django.urls import reverse

# Create your tests here.
from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains

@pytest.fixture
def video(db):
    v = Video(slug='motivacao', titulo='Vídeo Solo Leveling', vimeo_id='713312782')
    v.save()
    return v

@pytest.fixture
def resp(client, video):
    return client.get(reverse(('aperitivos:video'), args=('video.slug',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/713312782')
