from __future__ import unicode_literals

from django.urls import re_path
from infranil.views import InfranilView

urlpatterns = [
    re_path(r'^infranil/(?P<path>.*)$',
            InfranilView.as_view(base_dir="infranil/test/")),
]
