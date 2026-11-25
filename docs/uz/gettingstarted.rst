.. picozero: a library for controlling Raspberry Pi Pico GPIO pins with MicroPython
..
.. SPDX short identifier: MIT

=============
Ishni boshlash
=============

Mu yordamida o'rnatish
=====================

Talablar
--------

Windows yoki macOS kompyuteri (`Mu Editor`_\ o'rnatilgan).

.. _Mu Editor: https://github.com/roboticsware/mu/releases/latest

MicroPython rejimini tanlash
---------------------------

Mu-ni oching va yuqori chap burchakdagi **Rejim** tugmasini bosing. **RPi Pico**\ -ni tanlang va **OK** tugmasini bosing.

.. image:: /images/mu-select-mode.jpg
    :alt: Mu Editor-da RPi Pico rejimini tanlash

Mu-da PyPI-dan picozero-ni o'rnatish
------------------------------------

Mu-da picozero-rw ni o'rnatish uchun **MicroPython paketlari** tugmasini bosing.

.. image:: /images/mu-packages-button.jpg
    :alt: Mu-dagi MicroPython paketlari bo'limini tanlash

`picozero-rw`\ ni qidiring va **Qidirish** tugmasini bosing.

.. image:: /images/mu-search-picozero.jpg
    :alt: Mu paket menejerida picozero-rw ni qidirish

Paketni yuklab olish va qurilmangizga o'rnatish uchun **O'rnatish** tugmasini bosing.

.. image:: /images/mu-install-package.jpg
    :alt: Mu paket menejerida o'rnatish tugmasini bosish

Mu yordamida qo'lda o'rnatish
============================

picozero-ni Mu fayl menejeri yordamida ``picozero`` paket papkasini Raspberry Pi Pico-ga nusxalash orqali o'rnatish mumkin.

Fayl menejerini ochish uchun **Fayllar** tugmasini bosing.

.. image:: /images/mu-files-button.jpg
    :alt: Mu-dagi Fayllar tugmasini bosish

Mu-dagi **Kompyuteringizdagi fayllar** oynasidagi ``pico_lib`` papkasidan ``picozero`` papkasini toping va uni **Files on your device** oynasiga (yoki ``lib`` papkasiga) nusxalang.

.. image:: /images/mu-drag-and-drop.jpg
    :alt: Mu-da picozero papkasini kompyuterdan qurilmaga sudrab olib qo'yish

Ishni boshlash
=============

Thonny orqali o'rnatish
======================

Talablar
--------

`Thonny Python IDE`_ o'rnatilgan Windows, macOS yoki Linux kompyuteri.

.. _Thonny Python IDE: https://thonny.org/

Thonny-ni qanday o'rnatish haqida ma'lumotni `Raspberry Pi Pico-ga kirish qo'llanmasi`_\ dan topishingiz mumkin.

.. _Raspberry Pi Pico-ga kirish qo'llanmasi: https://learning-admin.raspberrypi.org/en/projects/introduction-to-the-pico/2

Thonny o'rnatilgandan so'ng, siz oxirgi MicroPython proshivkasidan foydalanayotganingizga ishonch hosil qilishingiz kerak. Raspberry Pi Pico MicroPython proshivkasini o'rnatish yoki yangilash haqida batafsil ma'lumotni `Pico qo'llanmasi`_\ dan topishingiz mumkin.

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

PyPI-dan `picozero-rw` ni qidiring.

.. image:: /images/thonny-packages-picozero.jpg
    :alt: Thonny-dagi Manage Packages oynasining Search maydoniga picozero kiritilgan holati

Paketni yuklab olish uchun **install** tugmasini bosing.

.. image:: /images/thonny-install-package.jpg
    :alt: Manage Packages oynasida ko'rsatilgan picozero paketi haqida ma'lumot

Thonny yordamida qo'lda o'rnatish
================================

picozero Raspberry Pi Pico-da xotira sarfini kamaytirish uchun modulli paket (``picozero/``) shaklida tuzilgan. Thonny fayl menejeri yordamida butun ``picozero`` papkasini Raspberry Pi Pico-ga yuklab qo'lda o'rnatishingiz mumkin.

**View** menyusida **Files** varianti belgilanganligiga ishonch hosil qiling. Bu sizga fayllarni ko'rish imkonini beradi.

.. image:: /images/thonny-view-files.jpg
    :alt: View menyusidan tanlangan Files varianti

picozero `GitHub repozitoriysi`_\ ni klonlang yoki ZIP arxivni yuklab olib kompyuteringizda arxivdan chiqaring.

.. only:: html

   .. raw:: html

      <p>
        <a href="https://github.com/roboticsware/picozero/archive/refs/heads/main.zip" download>
          ⬇️ picozero (ZIP)-ni yuklab olish
        </a>
      </p>

.. only:: not html

   ``picozero`` (ZIP)-ni yuklab olish:
   https://github.com/roboticsware/picozero/archive/refs/heads/main.zip

.. _GitHub repozitoriysi: https://github.com/roboticsware/picozero

Thonny-da klonlangan yoki arxivdan chiqarilgan katalogga o'ting va ``picozero`` papkasini (``__init__.py``, ``core.py``, ``led.py``, ``oled.py`` va boshqalar joylashgan) toping.

.. image:: /images/thonny-navigate-downloads.jpg

``picozero`` papkasini o'ng tugma bilan bosing va **Upload to /** (yoki **Upload to /lib**) variantini tanlang. Raspberry Pi Pico-da ``picozero`` papkasi ko'rinishi kerak.

.. image:: /images/thonny-upload-files.jpg
    :alt: Fayl menyusida tanlangan "Upload to /" varianti
.. image:: /images/thonny-copy-picozero.jpg
    :alt: Raspberry Pi Pico fayl ko'ruvchisida ko'rsatilgan picozero paketi.

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
