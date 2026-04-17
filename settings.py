# Minimal Django settings for pytest

SECRET_KEY = "test-secret-key"

DEBUG = True

USE_TZ = True

# In-memory SQLite (fast, perfect for tests)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Only what's needed
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",

    # Your apps
    "drzewo",
    "kalendarz",
    "kodeks",
    "mapa",
    "panel_wm",
    "piny",
    "skarbiec",
    "spiewnik",

]

# Required minimal config
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"