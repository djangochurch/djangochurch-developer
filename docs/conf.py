# -*- coding: utf-8 -*-

# -- General configuration -----------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Django Church Developer'
copyright = u'2014, Django Church'

# The short X.Y version.
version = 'current'
# The full version, including alpha/beta/rc tags.
release = 'current'

exclude_patterns = ['_build', 'pyenv']
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

import djangochurch_docs_theme
html_theme_path = [djangochurch_docs_theme.get_html_theme_path()]
html_theme = 'djangochurch_docs_theme'

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
    ('index', 'DjangoChurch.tex', u'Django Church Developer Documentation',
     u'Django Church', 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'djangochurch', u'Django Church Developer Documentation',
     [u'Django Church'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

texinfo_documents = [
    ('index', 'DjangoChurch', u'Django Church Developer Documentation',
     u'Django Church', 'DjangoChurch', 'One line description of project.',
     'Miscellaneous'),
]


# -- intersphinx ---------------------------------------------------------------

intersphinx_mapping = {
    'django': ('https://docs.djangoproject.com/en/1.7/',
               'https://docs.djangoproject.com/en/1.7/_objects/'),
}
intersphinx_cache_limit = 90  # days
