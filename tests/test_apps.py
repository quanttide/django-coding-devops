from django.test import SimpleTestCase, override_settings
from django.apps import apps


@override_settings(INSTALLED_APPS=['django_coding_devops.apps.DjangoCodingDevOpsConfig'])
class AppConfigTestCase(SimpleTestCase):
    def test_install_app(self):
        self.assertTrue(apps.is_installed('django_coding_devops'))
        app_config = apps.get_app_config('django_coding_devops')
        self.assertEqual('django_coding_devops', app_config.name)
