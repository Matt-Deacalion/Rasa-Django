"""Django pipeline settings."""

# ──┤ PIPELINE CONFIGURATION ├────────────────────────────────────────────────┐
PIPELINE_ENABLED = True

PIPELINE_JS = {
    'app': {
        'source_filenames': (
            'js/app.js',
        ),
        'output_filename': 'js/app.js',
        'template_name': 'js-tag',
    },
}

PIPELINE_CSS = {
    'app': {
        'source_filenames': {
            'css/app.css',
        },
        'output_filename': 'css/app.css',
        'template_name': 'css-tag',
    },
}
# ────────────────────────────────────────────────────────────────────────────┘
