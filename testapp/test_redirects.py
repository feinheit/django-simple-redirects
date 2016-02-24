from __future__ import unicode_literals

from django.test import TestCase

from sane_redirects.models import Redirect


class RedirectsTestCase(TestCase):
    def test_redirects(self):
        r = Redirect.objects.create(
            old_path='/something/',
            new_path='/something-else/',
        )

        self.assertEqual(
            '%s' % r,
            '/something/ ---> /something-else/',
        )

        self.assertRedirects(
            self.client.get('/something/'),
            '/something-else/',
        )
        self.assertRedirects(
            self.client.get('/something'),
            '/something-else/',
        )

        self.assertContains(
            self.client.get('/something-else/'),
            'Hello',
        )

        self.assertContains(
            self.client.get('/does-not-exist/'),
            'Not found',
            status_code=404,
        )

        self.assertContains(
            self.client.get('/does-not-exist'),
            'Not found',
            status_code=404,
        )
