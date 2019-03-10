import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dev_project.settings'
import django
django.setup()


project = 'BD Teamsport'
copyright = '2019, Chris Gough'
author = 'Chris Gough'

version = ''
release = '0.1'


extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    'sphinx.ext.autodoc'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = None
html_theme = 'alabaster'
html_static_path = ['_static']
latex_elements = {
    'papersize': 'a4paper',
}

latex_documents = [
    (master_doc, 'BDTeamsport.tex', 'BD Teamsport Documentation',
     'Chris Gough', 'manual'),
]


# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BDTeamsport', 'BD Teamsport Documentation',
     author, 'BDTeamsport', 'One line description of project.',
     'Miscellaneous'),
]
