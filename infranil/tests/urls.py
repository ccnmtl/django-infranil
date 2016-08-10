from __future__ import unicode_literals

from django.conf.urls import url
from infranil.views import InfranilView

urlpatterns = [
    url(r'^infranil/(?P<path>.*)$',
        InfranilView.as_view(base_dir="infranil/test/")),
]
