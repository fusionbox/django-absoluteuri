django-absoluteuri
==================

.. image:: https://travis-ci.org/fusionbox/django-absoluteuri.png?branch=master
    :target: https://travis-ci.org/fusionbox/django-absoluteuri

Absolute URI functions and template tags for Django.


Why
---

There are times when you need to output an absolute URL (for example, inside an
email), but you don't always have access to the request. These utilities use
the Sites Framework if available in order to create absolute URIs.


Installation
------------

Install django-absoluteuri::

    pip install django-absoluteuri

Then add it to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'django.contrib.sites',
        'absoluteuri',
    )

django-absoluteuri requires the `Sites Framework
<https://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_ to be in
``INSTALLED_APPS`` well and configured as well.


Settings
--------

The protocol of the uris returned by this library defaults to ``http``.  You
can specify the protocol with the ``ABSOLUTEURI_PROTOCOL`` setting.

.. code:: python

    # settings.py
    ABSOLUTEURI_PROTOCOL = 'https'

    # Elsewhere
    >>> absoluteuri.build_absolute_uri('/some/path/')
    'https://example.com/some/path/'


Template Tags
-------------

There are two template tags, ``absoluteuri`` and ``absolutize``.
``absoluteuri`` works just like the ``url`` tag, but that it outputs absolute
URLs.

.. code:: html+django

    {% load absoluteuri %}

    <a href="{% absoluteuri 'my_view' kwarg1='foo' kwarg2='bar' %}">click here</a>


``absolutize`` will take a relative URL and return an absolute URL.

.. code:: html+django

    {% load absoluteuri %}

    <a href="{% absolutize url_from_context %}">click here</a>


Functions
---------

There are also two functions that django-absoluteuri provides,
``build_absolute_uri`` and ``reverse``, which are equivalents of
``request.build_absolute_url`` and ``urlresolvers.reverse``.

.. code:: python

    >>> import absoluteuri

    >>> my_relative_url = '/path/to/somewhere/'
    >>> absoluteuri.build_absolute_uri(my_relative_url)
    'http://example.com/path/to/somewhere/'
    >>> absoluteuri.reverse('viewname', kwargs={'foo': 'bar'})
    'http://example.com/path/to/bar/'
