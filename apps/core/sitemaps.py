from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['core:home','core:privacy_policy', 'core:terms_of_use']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    """Sitemap for project pages"""
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # List of your project slugs
        return [
            'the-tide-grand-nawong',
            'the-tide-grand-phutthaphum',
            'the-tide-privilege-therdphra-kiat',
        ]

    def location(self, item):
        return reverse('core:project_plans', kwargs={'slug': item})