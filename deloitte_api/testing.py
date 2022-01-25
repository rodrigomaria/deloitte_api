from deloitte_api.settings import *  # noqa

TEST_RUNNER = "xmlrunner.extra.djangotestrunner.XMLTestRunner"
TEST_OUTPUT_DIR = "./reports/"
TEST_OUTPUT_FILE_NAME = "unit.xml"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "deloitte_api.sqlite3",  # noqa
    }
}

INSTALLED_APPS += ["behave_django"]  # noqa

DEBUG = False
