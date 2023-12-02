========================================
Welcome to aiogram-i18n's documentation!
========================================


.. image:: https://img.shields.io/pypi/v/aiogram-i18n.svg
    :target: https://pypi.python.org/pypi/aiogram-i18n


.. image:: https://img.shields.io/pypi/pyversions/aiogram-i18n.svg


.. image:: https://img.shields.io/pypi/l/aiogram-i18n.svg


.. image:: https://img.shields.io/pypi/dm/aiogram-i18n.svg


.. image::
    https://readthedocs.org/projects/aiogram-i18n/badge/?version=latest
    :target: https://aiogram-i18n.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


**aiogram_i18n**, an unrivalled middleware for Telegram bot internationalization,
breathes life into bots, enabling diverse interactions in multiple languages,
while adeptly managing user context, paving the way for a truly engaging and
immersive user experience irrespective of language preference, and providing robust
support for both Fluent and GNU gettext localization systems,
thereby offering flexibility in translation file format selection,
streamlining the translation process, and making the creation of multilingual bots
an achievable goal for developers.

Installation
============

To install aiogram-i18n without any backends:

.. code-block:: bash

    pip install aiogram-i18n

If you need help with what backend to choose, read :ref:`Backends`.


To use FluentCompileCore
------------------------

To use `fluent-compiler <https://pypi.org/project/fluent-compiler/>`_  backend
(:class:`aiogram_i18n.cores.fluent_compile_core.FluentCompileCore`) install it:

.. code-block:: bash

    pip install aiogram-i18n[compiler]

To use FluentRuntimeCore
------------------------

To use `Fluent.runtime <https://pypi.org/project/fluent.runtime/>`_ backend
(:class:`aiogram_i18n.cores.fluent_runtime_core.FluentRuntimeCore`) install it:

.. code-block:: bash

    pip install aiogram-i18n[runtime]

To use GNU gettext
------------------

To use `gettext <https://pypi.org/project/gettext/>`_ backend
(:class:`aiogram_i18n.cores.gnu_text_core.py.GettextCore`) install it:

.. code-block:: bash

    pip install aiogram-i18n[gettext]

Usage example
=============

.. literalinclude:: ../examples/mre.py
    :language: python
    :linenos:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :caption: Contents:

   backends/index
   poem
