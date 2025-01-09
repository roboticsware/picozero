picozero-rw
===========

|pypibadge| |docsbadge|

A beginner-friendly library to help you use common electronics components with the Raspberry Pi Pico.

This is a fork of the `origin picozero library. <https://github.com/RaspberryPiFoundation/picozero>`_


.. code-block:: python

    from picozero import LED, Button

    led = LED(1)
    button = Button(2)

    button.when_pressed = led.on
    button.when_released = led.off

Status
------

Beta. There will be bugs and issues. API changes are likely. More devices will be added over time.

Documentation
-------------

Documentation is available at `picozero-rw.readthedocs.io <https://picozero-rw.readthedocs.io>`_:

- `Installation and getting started guide <https://picozero-rw.readthedocs.io/en/latest/gettingstarted.html>`_
- `Recipes and how-to's <https://picozero-rw.readthedocs.io/en/latest/recipes.html>`_
- `API <https://picozero-rw.readthedocs.io/en/latest/api.html>`_
- `Example code <https://github.com/roboticsware/picozero/tree/master/docs/examples>`_

Code
----

The code and project is at `github.com/roboticsware/picozero <https://github.com/roboticsware/picozero>`_. 

Issues can be raised at `github.com/roboticsware/picozero/issues <https://github.com/roboticsware/picozero/issues>`_ (see `Contributing <https://picozero-rw.readthedocs.io/en/latest/contributing.html>`_).

The latest distribution is available at `pypi.org/project/picozero-rw/ <https://pypi.org/project/picozero-rw/>`_.

Thanks
------

picozero is inspired by `gpiozero <https://gpiozero.readthedocs.io/en/stable/>`_ (and reuses some of its underlying structure), but is, by design, lighter weight and aligned with the Raspberry Pi Pico. Thank you to everyone who has contributed to the gpiozero project.

.. |pypibadge| image:: https://badge.fury.io/py/picozero-rw.svg
   :target: https://badge.fury.io/py/picozero-rw
   :alt: Latest Version

.. |docsbadge| image:: https://readthedocs.org/projects/picozero-rw/badge/
   :target: https://readthedocs.org/projects/picozero-rw/
   :alt: Docs
