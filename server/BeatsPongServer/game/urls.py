from django.urls import path, re_path
from . import views
from .BPSlaveMaster import BPSlaveMaster

app_name = 'game'

urlpatterns = [
    re_path('ws/game/pong$', BPSlaveMaster.as_asgi()),
]