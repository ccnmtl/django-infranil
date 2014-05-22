from django.conf.urls import patterns
from infranil.views import InfranilView

urlpatterns = patterns(
    '',
    (r'^infranil/(?P<path>.*)$',
     InfranilView.as_view(base_dir="infranil/test/")),
)
