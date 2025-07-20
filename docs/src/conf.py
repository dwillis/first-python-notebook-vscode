from datetime import datetime

extensions = [
    "myst_nb",
    "sphinx_multitoc_numbering",
]
source_suffix = ".md"
master_doc = "index"

project = 'First Python Notebook VSCode'
year = datetime.now().year
copyright = f'{year}  Derek Willis'

exclude_patterns = ["_build"]

html_theme = "alabaster"
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
html_theme_options = {
    "canonical_url": f"https://first-python-notebook-vscode.readthedocs.io",
}

html_static_path = ['_static']

pygments_style = 'sphinx'

# Notebook execution configuration
jupyter_execute_notebooks = "force"
execution_timeout = 60
