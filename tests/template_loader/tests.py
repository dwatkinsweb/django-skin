import os

from django.template import Context, TemplateDoesNotExist
from django.template.loader import get_template
from django.test.utils import override_settings
from django.test import TransactionTestCase

TEST_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(TEST_DIR, 'templates'),
)


class TemplateLoaderTests(TransactionTestCase):
    fixtures = ['testskin.json']

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.app_directories.Loader',
                                         'django.template.loaders.app_directories.Loader'))
    def test_appdirectory_loader(self):
        template = get_template("template_loader/hello.html")
        self.assertEqual(template.render(Context()), "Hello! (Django app templates)")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.app_directories.Loader',
                                         'django.template.loaders.app_directories.Loader'),
                       SKIN_NAME='testskin')
    def test_appdirectory_loader_skin(self):
        template = get_template("template_loader/hello.html")
        self.assertEqual(template.render(Context()), "Hello! (Django app skins)")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.app_directories.Loader',
                                         'django.template.loaders.app_directories.Loader'),
                       SKIN_NAME='asdf')
    def test_appdiretory_loader_bad_skin(self):
        template = get_template("template_loader/hello.html")
        self.assertEqual(template.render(Context()), "Hello! (Django app templates)")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.app_directories.Loader',
                                         'django.template.loaders.app_directories.Loader'),
                       SKIN_NAME='asdf')
    def test_appdiretory_loader_not_found(self):
        self.assertRaises(TemplateDoesNotExist, get_template, "asdf.html")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.filesystem.Loader',
                                         'django.template.loaders.filesystem.Loader'),
                       TEMPLATE_DIRS=TEMPLATE_DIRS)
    def test_filesystem_loader(self):
        template = get_template("hello.html")
        self.assertEqual(template.render(Context()), "Hello! (Django filesystem templates)")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.filesystem.Loader',
                                         'django.template.loaders.filesystem.Loader'),
                       SKIN_NAME='testskin',
                       TEMPLATE_DIRS=TEMPLATE_DIRS)
    def test_filesystem_loader_skin(self):
        template = get_template("hello.html")
        self.assertEqual(template.render(Context()), "Hello! (Django filesystem skins)")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.filesystem.Loader',
                                         'django.template.loaders.filesystem.Loader'),
                       SKIN_NAME='asdf',
                       TEMPLATE_DIRS=TEMPLATE_DIRS)
    def test_filesystem_loader_bad_skin(self):
        template = get_template("hello.html")
        self.assertEqual(template.render(Context()), "Hello! (Django filesystem templates)")

    @override_settings(TEMPLATE_LOADERS=('skin.template.loaders.filesystem.Loader',
                                         'django.template.loaders.filesystem.Loader'),
                       SKIN_NAME='asdf',
                       TEMPLATE_DIRS=TEMPLATE_DIRS)
    def test_filesystem_loader_not_found(self):
        self.assertRaises(TemplateDoesNotExist, get_template, "asdf.html")
