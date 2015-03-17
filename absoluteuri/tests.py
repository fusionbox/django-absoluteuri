from django.test import TestCase
from django.template import Template, Context
from django.conf.urls import url


def view(request, *args, **kwargs):
    pass


urlpatterns = [
    url(r'^foo/$', view, name='view'),
    url(r'^foo/(?P<foo>\w+)/$', view, name='view'),
    url(r'^foo/(\d+)/$', view, name='view'),
]


class AbsoluteURITestCase(TestCase):
    def render_template(self, template, is_secure=False, **context_data):
        context = Context(context_data)
        return Template(template).render(context)

    def test_absoluteuri_tag(self):
        template = "{% load absoluteuri %}{% absoluteuri 'view' %}"
        rendered = self.render_template(template)
        self.assertEqual(rendered, 'http://example.com/foo/')

        kwarg_tmpl = "{% load absoluteuri %}{% absoluteuri 'view' foo='bar' %}"
        rendered2 = self.render_template(kwarg_tmpl)
        self.assertEqual(rendered2, 'http://example.com/foo/bar/')

        arg_tmpl = "{% load absoluteuri %}{% absoluteuri 'view' 12 %}"
        rendered3 = self.render_template(arg_tmpl)
        self.assertEqual(rendered3, 'http://example.com/foo/12/')

    def test_absolutize_tag(self):
        template = "{% load absoluteuri %}{% absolutize path %}"
        rendered = self.render_template(template, path='/url/path/')
        self.assertEqual(rendered, 'http://example.com/url/path/')
