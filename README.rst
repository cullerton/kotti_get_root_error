kotti_get_root_error
***********

This is an extension to Kotti that allows to add foo to your site.

|pypi|_
|downloads_month|_
|license|_
|build_status_stable|_

.. |pypi| image:: https://img.shields.io/pypi/v/kotti_get_root_error.svg?style=flat-square
.. _pypi: https://pypi.python.org/pypi/kotti_get_root_error/

.. |downloads_month| image:: https://img.shields.io/pypi/dm/kotti_get_root_error.svg?style=flat-square
.. _downloads_month: https://pypi.python.org/pypi/kotti_get_root_error/

.. |license| image:: https://img.shields.io/pypi/l/kotti_get_root_error.svg?style=flat-square
.. _license: http://www.repoze.org/LICENSE.txt

.. |build_status_stable| image:: https://img.shields.io/travis//kotti_get_root_error/production.svg?style=flat-square
.. _build_status_stable: http://travis-ci.org//kotti_get_root_error

`Find out more about Kotti`_

Development happens at https://github.com//kotti_get_root_error

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    kotti.configurators =
        kotti_get_root_error.kotti_configure

Database upgrade
================

If you are upgrading from a previous version you might have to migrate your
database.  The migration is performed with `alembic`_ and Kotti's console script
``kotti-migrate``. To migrate, run
``kotti-migrate upgrade --scripts=kotti_get_root_error:alembic``.

For integration of alembic in your environment please refer to the
`alembic documentation`_. If you have problems with the upgrade,
please create a new issue in the `tracker`_.

Development
===========

|build_status_master|_

.. |build_status_master| image:: https://img.shields.io/travis//kotti_get_root_error/master.svg?style=flat-square
.. _build_status_master: http://travis-ci.org//kotti_get_root_error

Contributions to kotti_get_root_error are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _alembic: http://pypi.python.org/pypi/alembic
.. _alembic documentation: https://alembic.readthedocs.io/en/latest/index.html
.. _tracker: https://github.com//kotti_get_root_error/issues
.. _Github repository: https://github.com//kotti_get_root_error
