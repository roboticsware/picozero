.. picozero: a library for controlling Raspberry Pi Pico GPIO pins with MicroPython
..
.. SPDX short identifier: MIT

=============
Ishni boshlash
=============

Thonny orqali o'rnatish
======================

Talablar
--------

`Thonny Python IDE`_ o'rnatilgan Windows, macOS yoki Linux kompyuteri.

.. _Thonny Python IDE: https://thonny.org/

Thonny-ni qanday o'rnatish haqida ma'lumotni `Raspberry Pi Pico-ga kirish qo'llanmasi`_dan topishingiz mumkin.

.. _Raspberry Pi Pico-ga kirish qo'llanmasi: https://learning-admin.raspberrypi.org/en/projects/introduction-to-the-pico/2

Thonny o'rnatilgandan so'ng, siz oxirgi MicroPython proshivkasidan foydalanayotganingizga ishonch hosil qilishingiz kerak. Raspberry Pi Pico MicroPython proshivkasini o'rnatish yoki yangilash haqida batafsil ma'lumotni `Pico qo'llanmasi`_dan topishingiz mumkin.

.. _Pico qo'llanmasi: https://learning-admin.raspberrypi.org/en/projects/introduction-to-the-pico/3

MicroPython interpretatorini tanlash
------------------------------------

Siz Thonny-da foydalanayotgan interpretatorni ekranning pastki o'ng burchagidagi kerakli variantni tanlash orqali o'zgartirishingiz mumkin. **MicroPython (Raspberry Pi Pico)** tanlanganligiga ishonch hosil qiling.

.. image:: /images/thonny-switch-interpreter.jpg
    :alt: Thonny IDE pastki o'ng burchagidagi interpretator menyusidan MicroPython (Raspberry Pi Pico)-ni tanlash

Thonny-da PyPI-dan picozero-ni o'rnatish
----------------------------------------

Thonny-da picozero-ni o'rnatish uchun **Tools** > **Manage packages...** ni tanlang.

.. image:: /images/thonny-manage-packages.jpg
    :alt: Thonny-dagi Tools menyusidan Manage Packages-ni tanlash

PyPI-dan `picozero` ni qidiring.

.. image:: /images/thonny-packages-picozero.jpg
    :alt: Thonny-dagi Manage Packages oynasining Search maydoniga picozero kiritilgan holati

Paketni yuklab olish uchun **install** tugmasini bosing.

.. image:: /images/thonny-install-package.jpg
    :alt: Manage Packages oynasida ko'rsatilgan picozero paketi haqida ma'lumot

Qo'lda o'rnatish
===============

picozero-ni ``picozero.py`` kodini Raspberry Pi Pico-ga nusxalash orqali ham o'rnatish mumkin.

picozero `GitHub repozitoriysi`_ni klonlang yoki `picozero.py`_ faylidan kodni nusxalab oling va uni asosiy kompyuteringizda saqlang.

.. _GitHub repozitoriysi: https://github.com/roboticsware/picozero
.. _picozero.py: https://raw.githubusercontent.com/roboticsware/picozero/refs/heads/main/picozero/picozero.py

picozero.py deb nomlangan yangi fayl yarating, kodni faylga nusxalang va uni Raspberry Pi Pico-da saqlang.

Thonny yordamida picozero.py nusxasini ko'chirish
------------------------------------------------

Shu bilan bir qatorda, ``picozero.py`` faylini Raspberry Pi Pico-ga o'tkazish uchun Thonny fayl menejeridan foydalanishingiz mumkin.

**View** menyusida **Files** varianti belgilanganligiga ishonch hosil qiling. Bu sizga fayllarni ko'rish imkonini beradi.

.. image:: /images/thonny-view-files.jpg
    :alt: View menyusidan tanlangan Files varianti

picozero `GitHub repozitoriysi`_ni klonlang yoki `picozero.py`_ faylidan kodni nusxalab oling va uni asosiy kompyuteringizda saqlang.

.. _GitHub repozitoriysi: https://github.com/roboticsware/picozero
.. _picozero.py: https://raw.githubusercontent.com/roboticsware/picozero/refs/heads/main/picozero/picozero.py

Thonny-da klonlangan katalogga yoki faylni saqlagan joyingizga boring va ``picozero.py`` faylini toping.

.. image:: /images/thonny-navigate-downloads.jpg

Faylni o'ng tugma bilan bosing va **Upload to /** variantini tanlang. Raspberry Pi Pico-da ``picozero.py`` faylining nusxasini ko'rishingiz kerak.

.. image:: /images/thonny-upload-files.jpg
    :alt: picozero.py fayl menyusida tanlangan "Upload to /" varianti
.. image:: /images/thonny-copy-picozero.jpg
    :alt: Raspberry Pi Pico fayl ko'ruvchisida ko'rsatilgan picozero.py fayli.

Ichki LED-ni boshqarish uchun dastur yozish
==========================================

Quyidagi kod ichki LED-ni soniyasiga bir marta chastotada miltillatadi.::

    from picozero import pico_led
    from time import sleep

    while True:
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)

Dasturni kompyuteringizda ishga tushirish
-----------------------------------------

Dasturni kompyuteringizdan ishga tushirishni tanlashingiz mumkin.

**Run current script** tugmasini bosing.

.. image:: /images/run-current-script.jpg

Skriptni **This computer**-da saqlashni tanlang va fayl nomini kiriting.

.. image:: /images/save-this-computer.png

Dasturni Raspberry Pi Pico-da ishga tushirish
---------------------------------------------

Dasturni Raspberry Pi Pico-dan ishga tushirishni tanlashingiz mumkin.

**Run current script** tugmasini bosing.

.. image:: /images/run-current-script.jpg

Skriptni **Raspberry Pi Pico**-da saqlashni tanlang va fayl nomini kiriting.

.. image:: /images/save-this-raspberry-pi-pico.png

Agar faylni ``main.py`` deb nomlasangiz, u Pico-ga quvvat berilganda avtomatik ravishda ishga tushadi.
