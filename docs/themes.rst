Themes
======


What themes are available?
--------------------------

We provide the following themes as base templates for Django Church. Each of
them contains a ``static`` and ``templates`` directory, with all the files
needed for the standard Django Church applications:

* Bold_
* Fresh_
* Calm_
* House_
* Light_

.. _Bold: https://github.com/djangochurch/djangochurch-theme-bold
.. _Fresh: https://github.com/djangochurch/djangochurch-theme-fresh
.. _Calm: https://github.com/djangochurch/djangochurch-theme-calm
.. _House: https://github.com/djangochurch/djangochurch-theme-house
.. _Light: https://github.com/djangochurch/djangochurch-theme-light

Theme installation
------------------

We'll use the House_ theme as an example.

In the root directory of your Django Church project, run the following
commands:

.. code-block:: console

    $ curl -sL https://github.com/djangochurch/djangochurch-theme-house/tarball/master | tar zxv
     ...
    x djangochurch-djangochurch-theme-house-1852fc3/templates/pages/
    x djangochurch-djangochurch-theme-house-1852fc3/templates/pages/default.html
    $ mv djangochurch-djangochurch-theme-house-* theme

Simply replace ``house`` with one of the other theme names to install another
theme.

Theme customisation
-------------------

If you want to change the HTML files or other static files for a theme, we
recommend that you copy the file from the theme directory into your project
directory before editing it. By default Django will use templates from the site
template directory before the theme directory.

As an example, if your project was ``mychurch``, you'd copy the original
``theme/templates/base.html`` to ``mychurch/templates/base.html``.
