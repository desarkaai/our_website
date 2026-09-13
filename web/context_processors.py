"""
Template context shared by every page.
"""
import os
from pathlib import Path

from django.conf import settings


def _static_version():
    """Newest modification time across our CSS and JS, so a changed file gets a new URL.

    Browsers cache /static/ assets aggressively in development; appending ?v=<this>
    makes them fetch the new file as soon as it changes. Production also hashes
    filenames through ManifestStaticFilesStorage, so the query string is harmless there.
    """
    newest = 0
    for directory in getattr(settings, 'STATICFILES_DIRS', []):
        for sub in ('css', 'js'):
            folder = Path(directory) / sub
            if folder.is_dir():
                for f in folder.iterdir():
                    if f.is_file():
                        newest = max(newest, int(f.stat().st_mtime))
    return str(newest or 1)


def static_version(request):
    # On Vercel the deployed commit is the most reliable version: file times inside a
    # serverless bundle are not meaningful, and static/ may not be bundled at all.
    commit = os.environ.get('VERCEL_GIT_COMMIT_SHA', '')
    if commit:
        return {'STATIC_VERSION': commit[:12]}
    # Recomputed per request in DEBUG so edits show up without a restart; cached otherwise.
    if settings.DEBUG:
        return {'STATIC_VERSION': _static_version()}
    global _CACHED
    try:
        return {'STATIC_VERSION': _CACHED}
    except NameError:
        _CACHED = _static_version()
        return {'STATIC_VERSION': _CACHED}
