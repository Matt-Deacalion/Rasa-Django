"""Django pipeline settings."""

from .base import BOWER_COMPONENTS_ROOT

# ──┤ PIPELINE CONFIGURATION ├────────────────────────────────────────────────┐
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_ENABLED = True

PIPELINE_COMPILERS = (
    'pipeline_compass.compass.CompassCompiler',
)

PIPELINE_COMPASS_ARGUMENTS = '-I {}'.format(
    str(BOWER_COMPONENTS_ROOT / 'foundation' / 'scss')
)

PIPELINE_JS = {
    'app': {
        'source_filenames': (
            'js/app.js',
        ),
        'output_filename': 'js/app.js',
        'template_name': 'js-tag',
    },
    'jquery': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js',
        ),
        'output_filename': 'js/jquery.js',
        'template_name': 'js-tag',
    },
    'foundation': {
        'source_filenames': (
            'bower_components/foundation/js/foundation.js',
        ),
        'output_filename': 'js/foundation.js',
        'template_name': 'js-tag',
    },
    'modernizr': {
        'source_filenames': (
            'bower_components/modernizr/modernizr.js',
        ),
        'output_filename': 'js/modernizr.js',
        'template_name': 'js-tag',
    },
    'underscore': {
        'source_filenames': (
            'bower_components/underscore/underscore.js',
        ),
        'output_filename': 'js/underscore.js',
        'template_name': 'js-tag',
    },
}

PIPELINE_CSS = {
    'app': {
        'source_filenames': {
            'scss/app.scss',
        },
        'output_filename': 'css/app.css',
        'template_name': 'css-tag',
    },
}
# ────────────────────────────────────────────────────────────────────────────┘
