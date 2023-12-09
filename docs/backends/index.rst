.. _Backends:

========
Backends
========

`aiogram-i18n` supports many backends of translation and localization systems,
so you can use any of them to localize your bot.

Fluent runtime
==============

`Fluent.runtime <https://pypi.org/project/fluent.runtime/>`_ is a part of Project Fluent,
which is a localization system developed by Mozilla for natural-sounding translations.
It's designed to unleash the expressive power of the natural language.

If you want to use Fluent it's recommended to use `fluent_compile` instead of runtime
as it's the most efficient way to use Fluent in Python.

Pros of using fluent.runtime
----------------------------

- Fluent leverages Unicode and handles complex grammatical cases and gender.
- It works on a wide range of platforms and operating systems.
- The fluent syntax is very readable which makes it easier for localizers to understand.
- It handles placeholders and markup with ease.

Cons of using fluent.runtime
----------------------------

- Fluent.runtime is still young compared to gettext, therefore the community and
support aren’t as extensive.
- Its complexity and design may be way above what small projects need.

fluent.runtime
======================

.. code-block:: bash

    pip install aiogram-i18n[runtime]

Fluent compile
==============

`fluent-compiler <https://pypi.org/project/fluent-compiler/>`_ is a Python implementation
of Project Fluent, a localization framework designed to unleash the entire expressive
power of natural language translations.

it is mainly used to compile FTL files to AST (Abstract Syntax Tree).
It is very useful for run-time parsing.

Pros of using fluent-compiler
-----------------------------

- It's beneficial for handling FTL files on the runtime and compiling them into AST for efficient use.

Cons of using fluent-compiler
-----------------------------

- As with Fluent.runtime, fluent-compiler is relatively new and as such doesn't have
as extensive resources or community.

Install fluent-compiler
-----------------------

.. code-block:: bash

    pip install aiogram-i18n[compiler]


GNU gettext
===========

`GNU gettext <https://docs.python.org/3/library/gettext.html>`_ is an
internationalization (i18n) and localization (l10n) framework commonly used in open
source projects. It works by providing string function calls in your code that wraps strings
meant for user interface, and then it generates .po files which are human-readable and editable,
containing the actual translations.

Pros of using GNU gettext
-------------------------

- Gettext is widely used and has a large community. It means there are many tools,
guides and supports available for it.
- Offers good support for plurals.
- It handles the translation outside of your code which makes your code cleaner.
- Gettext is part of the GNU Project, being present in most of the Linux Distros.

Cons of using GNU gettext
-------------------------

- It can be more difficult to provide context for your strings, because the only context
you can give for your source strings are comments in your code.
- Its complexity can be intimidating for non-technical translators.

Install GNU gettext
-------------------

.. code-block:: bash

    pip install aiogram-i18n[gettext]


.. toctree::

    fluent_compile
    fluent_runtime
    gettext
    base
