Vagrant
=======

To get you up and running quickly and easily, a `Django Church Vagrantfile`_ is
available for usage with Vagrant__ and Virtualbox_.

.. _Django Church Vagrantfile: https://github.com/djangochurch/djangochurch-vagrant
.. __: https://www.vagrantup.com/
.. _Virtualbox: https://www.virtualbox.org/


Prerequisites
-------------

* Installed Virtualbox_.
* Installed Vagrant_.


Mac OS X
--------

Open up terminal, and run the following commands:

.. code-block:: console

    $ git clone https://github.com/djangochurch/djangochurch-vagrant.git
    Cloning into 'djangochurch-vagrant'...
    remote: Counting objects: 16, done.
    remote: Compressing objects: 100% (9/9), done.
    remote: Total 16 (delta 6), reused 16 (delta 6)
    Unpacking objects: 100% (16/16), done.
    Checking connectivity... done.
    $ cd djangochurch-vagrant
    $ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Importing base box 'ubuntu/trusty32'...
    ...

.. note::

    If you don't have the OS X developer tools installed, a pop-up may appear
    asking you to install them. Install the developer tools, then run the first
    command again.


The ``vagrant up`` command may take up to 15 minutes to run, but may take
longer on slower Internet connections.

Once ``vagrant up`` has completed, the ``sites`` directory in the
``djangochurch-vagrant`` directory will contain the 5 Django instances of
Django Church, each with a different theme. By default the sites should be
accessible at:

* Bold: `http://127.0.0.1:5001/ <http://127.0.0.1:5001/>`_
* Fresh: `http://127.0.0.1:5002/ <http://127.0.0.1:5002/>`_
* Calm: `http://127.0.0.1:5003/ <http://127.0.0.1:5003/>`_
* House: `http://127.0.0.1:5004/ <http://127.0.0.1:5004/>`_
* Light: `http://127.0.0.1:5005/ <http://127.0.0.1:5005/>`_

The Django admin panel is accessible at ``/admin/``, with the username and
password both set to admin.

All Django instances share the same database and media directory, so any
content added to one site will appear on all other sites, allowing you to
preview how your site could look with another theme.

Once you've finished, simply run:

.. code-block:: console

    $ vagrant destroy
        default: Are you sure you want to destroy the 'default' VM? [y/N] y
    ==> default: Forcing shutdown of VM...
    ==> default: Destroying VM and associated drives...
    ==> default: Running cleanup tasks for 'shell' provisioner...

Then Vagrant will stop the virtual machine running the sites.
