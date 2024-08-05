from __future__ import unicode_literals

from django.urls import re_path
from .views import InfranilView


urlpatterns = [
    re_path(r'^(?P<path>.*)$', InfranilView.as_view()),
]
