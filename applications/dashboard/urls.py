from django.contrib.sitemaps.views import sitemap as sitemap_view
from django.contrib.sitemaps import Sitemap
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse

from applications.dashboard import views


class DashboardSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['index', 'privacy']

    def location(self, item):
        return reverse(item)


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
