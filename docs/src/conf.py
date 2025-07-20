from datetime import datetime

extensions = [
    "myst_parser",
    "sphinx_multitoc_numbering",
]
source_suffix = ".md"
master_doc = "index"

project = 'First Python Notebook'
year = datetime.now().year
copyright = f'{year} Derek Willis'

exclude_patterns = ["_build"]

html_theme = "alabaster"
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
html_theme_options = {
    "canonical_url": f"https://palewi.re/docs/first-python-notebook/",
}

html_static_path = ['_static']

pygments_style = 'sphinx'
