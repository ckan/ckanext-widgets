.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/ckan/ckanext-widgets.svg?branch=master
    :target: https://travis-ci.org/ckan/ckanext-widgets

.. image:: https://coveralls.io/repos/ckan/ckanext-widgets/badge.png?branch=master
  :target: https://coveralls.io/r/ckan/ckanext-widgets?branch=master

.. image:: https://pypip.in/download/ckanext-widgets/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-widgets/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-widgets/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-widgets/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-widgets/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-widgets/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-widgets/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-widgets/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-widgets/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-widgets/
    :alt: License

=============
ckanext-widgets
=============

.. Some helper widgets to help render atom/rss feeds
   into CKAN themes. Provides additional default layouts for
   the CKAN front page




------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-widgets:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-widgets Python package into your virtual environment::

     pip install -e git+https://github.com/ckan/ckanext-widgets.git#egg=ckanext-widgets

3. Add ``widgets`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

    # Sets the the featured feed in the default layout widgets1
    ckanext.widgets.featured_feed = https://feeds.feedburner.com/ckanproject
    # you will also need to set, or change in the admin page
    ckan.homepage_style = widgets1


------------------------
Development Installation
------------------------

To install ckanext-widgets for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/ckan/ckanext-widgets.git
    cd ckanext-widgets
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.widgets --cover-inclusive --cover-erase --cover-tests
