picozero-rw
===========

|pypibadge| |docsbadge|

Raspberry Pi Pico bilan oddiy elektron komponentlardan foydalanishga yordam beradigan yangi boshlovchilar uchun qulay kutubxona.

Bu asl `picozero kutubxonasining <https://github.com/RaspberryPiFoundation/picozero>`_ forki hisoblanadi.


.. code-block:: python

    from picozero import LED, Button

    led = LED(1)
    button = Button(2)

    button.when_pressed = led.on
    button.when_released = led.off

Holati
------

Beta. Xatolar va muammolar bo'lishi mumkin. API o'zgarishlari ehtimoli bor. Vaqt o'tishi bilan ko'proq qurilmalar qo'shiladi.

Hujjatlar
---------

Hujjatlar `picozero-rw.readthedocs.io <https://picozero-rw.readthedocs.io>`_ saytida mavjud:

- `O'rnatish va ishni boshlash bo'yicha qo'llanma <https://picozero-rw.readthedocs.io/en/latest/uz/gettingstarted.html>`_
- `Retseptlar va "qanday qilish kerak" qo'llanmalari <https://picozero-rw.readthedocs.io/en/latest/uz/recipes.html>`_
- `API <https://picozero-rw.readthedocs.io/en/latest/uz/api.html>`_
- `Namuna kodlar <https://github.com/roboticsware/picozero/tree/master/docs/examples>`_

Kod
----

Kod va loyiha `github.com/roboticsware/picozero <https://github.com/roboticsware/picozero>`_ manzilida joylashgan.

Muammolarni `github.com/roboticsware/picozero/issues <https://github.com/roboticsware/picozero/issues>`_ sahifasida qoldirishingiz mumkin (`Hissa qo'shish <https://picozero-rw.readthedocs.io/en/latest/uz/contributing.html>`_ bo'limiga qarang).

Oxirgi tarqatilgan versiya `pypi.org/project/picozero-rw/ <https://pypi.org/project/picozero-rw/>`_ saytida mavjud.

Rahmat
------

picozero `gpiozero <https://gpiozero.readthedocs.io/en/stable/>`_ loyihasidan ilhomlangan (va uning ba'zi asosiy tuzilmalaridan foydalanadi), lekin u Raspberry Pi Pico bilan moslashgan holda yengilroq qilib ishlab chiqilgan. gpiozero loyihasiga hissa qo'shgan barchaga rahmat.

.. |pypibadge| image:: https://badge.fury.io/py/picozero-rw.svg
   :target: https://badge.fury.io/py/picozero-rw
   :alt: Oxirgi versiya

.. |docsbadge| image:: https://readthedocs.org/projects/picozero-rw/badge/
   :target: https://readthedocs.org/projects/picozero-rw/
   :alt: Hujjatlar
