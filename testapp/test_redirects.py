from django.test import TestCase

from sane_redirects.models import Redirect


class RedirectsTestCase(TestCase):
    def test_redirects(self):
        Redirect.objects.create(
            old_path='/something/',
            new_path='/something-else/',
        )

        response = self.client.get('/something/')
        self.assertRedirects(
            self.client.get('/something/'),
            '/something-else/',
            fetch_redirect_response=False,
        )
