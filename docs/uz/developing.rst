Ishlab chiqish
==============

picozero-ni yaratish (build) va joylashtirish (deploy) bo'yicha ko'rsatmalar.

Oldindan talablar
-----------------

picozero-ni yaratish va joylashtirish uchun kerakli bog'liqliklarni o'rnatishingiz kerak::

    pip3 install twine sphinx 

Yaratish (Build)
----------------

1. ``setup.py``, ``picozero/__init__.py`` va ``docs/conf.py`` fayllaridagi versiya raqamlarini yangilang.

2. ``docs/changelog.rst`` fayliga yangi versiya haqida ma'lumot qo'shing.

3. ``setup.py``-ni ishga tushiring va manba tarqatmasini (source distribution) yarating::

    python3 setup.py sdist

4. PyPI-ga yuklang::

    twine upload dist/*

5. Barcha o'zgarishlarni ``master`` tarmog'iga yuboring (push).

6. GitHub-da `release <https://github.com/roboticsware/picozero/releases>`_ (versiya) yarating va ``picozero-#-#-#.tar.gz`` manba faylini ushbu relizga yuklang.

Hujjatlar
---------

Hujjatlar sayti Sphinx yordamida yaratilgan. 

Sphinx-ni quyidagicha o'rnating::

    pip3 install sphinx

Hujjatlar yaratilishini sinab ko'rish uchun docs katalogidan quyidagi buyruqni ishga tushiring::

    $ ./make html

Veb-sayt docs/_build/html katalogida yaratiladi.

Hujjatlarni `picozero-rw.readthedocs.io`_ saytida ko'rish mumkin va ular GitHub-ga yuborilganda (push) avtomatik ravishda yaratiladi va joylashtiriladi.

.. _picozero-rw.readthedocs.io: https://picozero-rw.readthedocs.io

Sinovlar (Tests)
----------------

Sinovlar Raspberry Pi Pico-da ishlashga mo'ljallangan.

1. `picozero <https://pypi.org/project/picozero/>`_ paketini o'rnating.

2. `micropython-unittest <https://pypi.org/project/micropython-unittest/>`_ paketini o'rnating.

3. ``test_picozero.py`` faylini Pico-ga nusxalang.

4. ``test_picozero.py`` faylini ishga tushiring.

Agar biron bir sinov muvaffaqiyatsiz tugasa, batafsil xato xabarlarini ko'rish foydali bo'ladi. Xato xabarlarini ko'rish uchun Pico-dagi ``lib/unittest.py`` faylini o'zgartirishingiz kerak.

``run_class`` funksiyasidan quyidagi kodni toping::

    # Uncomment to investigate failure in detail
    #raise

``raise`` qatoridan izohni olib tashlang::

    # Uncomment to investigate failure in detail
    raise
