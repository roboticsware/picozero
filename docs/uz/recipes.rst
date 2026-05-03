Retseptlar
=========

Retseptlar picozero-dan qanday foydalanish bo'yicha misollarni taqdim etadi.

picozero-ni import qilish
-------------------------

.. currentmodule:: picozero

picozero-dan foydalanish uchun skriptingizning yuqori qismiga `import` qatorini qo'shishingiz kerak bo'ladi.

Faqat kerakli narsalarni vergul ``,`` bilan ajratib import qilishingiz mumkin::

    from picozero import pico_led, LED

Endi skriptingizda :obj:`~picozero.pico_led` va :class:`~picozero.LED`-dan foydalanishingiz mumkin::

    pico_led.on() # Raspberry Pi Pico-dagi LED-ni yoqish
    led = LED(14) # GP14 piniga ulangan LED-ni boshqarish
    led.on()
 
Shu bilan bir qatorda, butun picozero kutubxonasini import qilish mumkin::

    import picozero

Bunday holda, barcha picozero elementlariga murojaat qilishda prefiks qo'shilishi kerak::

    picozero.pico_led.on()
    led = picozero.LED(14)


Pico LED
--------

.. image:: /images/pico_led.svg
    :alt: Raspberry Pi Pico-ning ichki LED-iga GP25 yorlig'i biriktirilgan diagrammasi.

Raspberry Pi Pico-dagi LED-ni yoqish uchun:

.. literalinclude:: ../examples/pico_led.py

LED yonganini ko'rish uchun skriptingizni ishga tushiring.

:obj:`pico_led`-dan foydalanish quyidagiga teng::

    pico_led = LED(25) 

:obj:`pico_led`-dan :class:`LED` yordamida yaratilgan tashqi LED-lar kabi foydalanishingiz mumkin.

Pinlar xaritasi (Pin out)
-------------------------

Siz Raspberry Pi Pico-ning pinlari va ularning raqamlarini ko'rsatadigan *diagrammasini* chiqarishingiz mumkin.

.. literalinclude:: ../examples/print_pinout.py

::

            ---usb---
    GP0  1  |o     o| -1  VBUS
    GP1  2  |o     o| -2  VSYS
    GND  3  |o     o| -3  GND
    GP2  4  |o     o| -4  3V3_EN
    GP3  5  |o     o| -5  3V3(OUT)
    GP4  6  |o     o| -6           ADC_VREF
    GP5  7  |o     o| -7  GP28     ADC2
    GND  8  |o     o| -8  GND      AGND
    GP6  9  |o     o| -9  GP27     ADC1
    GP7  10 |o     o| -10 GP26     ADC0
    GP8  11 |o     o| -11 RUN
    GP9  12 |o     o| -12 GP22
    GND  13 |o     o| -13 GND
    GP10 14 |o     o| -14 GP21
    GP11 15 |o     o| -15 GP20
    GP12 16 |o     o| -16 GP19
    GP13 17 |o     o| -17 GP18
    GND  18 |o     o| -18 GND
    GP14 19 |o     o| -19 GP17
    GP15 20 |o     o| -20 GP16
            ---------

Svetodiodlar (LED)
------------------
 
.. image:: /images/pico_led_14_bb.svg
    :alt: GP14 va GND-ga ulangan sariq LED-li Raspberry Pi Pico diagrammasi.

Raspberry Pi Pico yordamida tashqi svetodiodlarni (LED) boshqarishingiz mumkin.

Miltillash
~~~~~~~~~~

:class:`LED`-ni yoqish va o'chirish:

.. literalinclude:: ../examples/led_on_off.py

:class:`LED`-ni yoqilganidan o'chirilganiga yoki o'chirilganidan yoqilganiga o'tkazish (toggle):

.. literalinclude:: ../examples/led_toggle.py

.. only:: html

   .. raw:: html

      <p>
        <a href="https://wokwi.com/projects/417606412375790593" target="_blank">
          🚀 Wokwi simulyatorida ishga tushirish
        </a>
      </p>

Shu bilan bir qatorda, :meth:`~picozero.LED.blink` metodidan foydalanishingiz mumkin.

.. literalinclude:: ../examples/led_blink.py

Yorqinlik
~~~~~~~~~

:class:`LED`-ning yorqinligini o'rnatish:

.. literalinclude:: ../examples/led_brightness.py

Puls effekti yaratish:

.. literalinclude:: ../examples/led_pulse.py

Shu bilan bir qatorda, :meth:`~picozero.LED.pulse` metodidan foydalanishingiz mumkin.

.. literalinclude:: ../examples/led_pulse_method.py

Tugmalar
--------

Raspberry Pi Pico-ga tugmalar va kalitlarni ulashingiz hamda ular bosilganligini aniqlashingiz mumkin.

:class:`Button` bosilganligini tekshirish:

.. literalinclude:: ../examples/button_is_pressed.py


Har safar :class:`Button` bosilganda funksiyani ishga tushirish:

.. literalinclude:: ../examples/button_function.py

.. note::

    ``button.when_pressed = led_on_off`` qatori ``led_on_off`` funksiyasini 
    darhol ishga tushirmaydi, balki tugma bosilganda chaqiriladigan funksiyaga 
    havola yaratadi. Tasodifan ``button.when_pressed = led_on_off()``-dan foydalanish 
    ``when_pressed`` harakatini :data:`None`-ga o'rnatadi (bu funksiyaning qaytarish qiymati), 
    bu esa tugma bosilganda hech narsa sodir bo'lmasligini anglatadi.

:class:`Button` bosilganda :obj:`pico_led`-ni yoqish va qo'yib yuborilganda o'chirish:

.. literalinclude:: ../examples/button_led.py

Sensorli teginish (Touch sensor)
--------------------------------

Kapasitiv sensorli teginish datchigi yordamida teginishni aniqlash:

.. literalinclude:: ../examples/touch_sensor.py

Teginish hodisalariga javob berish uchun qayta chaqiruvlardan (callbacks) foydalanish:

.. literalinclude:: ../examples/touch_sensor_callbacks.py

Harakat sensori (Motion sensor)
-------------------------------

PIR (Passive Infrared) sensori yordamida harakatni aniqlash:

.. literalinclude:: ../examples/motion_sensor.py

Harakat hodisalariga javob berish uchun qayta chaqiruvlardan (callbacks) foydalanish:

.. literalinclude:: ../examples/motion_sensor_callbacks.py

RGB svetodiodlar
----------------

:class:`RGBLED` yordamida ranglarni o'rnatish:

.. literalinclude:: ../examples/rgb_led.py

:meth:`~picozero.RGBLED.toggle` va :meth:`~picozero.RGBLED.invert`-dan foydalanish:

.. literalinclude:: ../examples/rgb_toggle_invert.py

Blink (Miltillash)
~~~~~~~~~~~~~~~~~~

Ranglar o'rtasida almashish uchun :meth:`~picozero.RGBLED.blink` metodidan foydalaning. Qaysi ranglar ishlatilishini va LED har bir rangda qancha turishini boshqarishingiz mumkin. `(0, 0, 0)` rangi o'chirilganligini bildiradi. 

Siz :meth:`~picozero.RGBLED.blink` ma'lum bir marta ishlashini va u tugaguncha kutishni yoki boshqa kodlar ishlashi uchun darhol qaytishini boshqarishingiz mumkin.

.. literalinclude:: ../examples/rgb_blink.py

Pulse (Puls)
~~~~~~~~~~~~

LED rangini asta-sekin o'zgartirish uchun :meth:`~picozero.RGBLED.pulse`-dan foydalaning. Standart bo'yicha u qizil va o'chirilgan, keyin yashil va o'chirilgan, keyin ko'k va o'chirilgan ranglar orasida puls beradi. 

.. literalinclude:: ../examples/rgb_pulse.py

Cycle (Sikl)
~~~~~~~~~~~~

:meth:`~picozero.RGBLED.cycle` uchun standart ranglar qizildan yashilga, yashildan ko'kka, keyin ko'kdan qizilga sikl bo'lib aylanadi. 

.. literalinclude:: ../examples/rgb_cycle.py

Potensiometr
------------

Potensiometr tomonidan bildirilgan qiymat, kuchlanish va foizni chop etish:

.. literalinclude:: ../examples/potentiometer.py

.. note::

    Thonny Python muharririda :meth:`print` chiqishini chizish uchun **View** > **Plotter**-ni tanlang. 

LED yorqinligini boshqarish uchun potensiometrdan foydalanish:

.. literalinclude:: ../examples/pot_led.py

Joystik
-------

Joystik potensiometrga o'xshaydi, shuning uchun joystikni boshqarish uchun Pot klassidan foydalanishimiz mumkin.

.. image:: /images/joystick.png
    :alt: Joystikka ulangan Raspberry Pi Pico diagrammasi

Joystikni minimal, o'rta va maksimal pozitsiyalariga o'tkazing.

.. literalinclude:: ../examples/joystick.py

Buzzer
------

Quvvat berilganda nota chalinadigan aktiv buzzerni boshqarish:

.. literalinclude:: ../examples/buzzer.py

Dinamik (Speaker)
-----------------

Turli xil tonlar yoki chastotalarni chala oladigan passiv buzzer yoki dinamikni boshqarish:

.. literalinclude:: ../examples/speaker.py

Kuyni chalish
~~~~~~~~~~~~~

Nota nomlari va davomiyliklaridan (bitlarda) iborat kuyni chalish: 

.. literalinclude:: ../examples/speaker_tune.py

Alohida notalarni chalish
~~~~~~~~~~~~~~~~~~~~~~~~~

Alohida notalarni chaling va vaqtni boshqaring yoki boshqa harakatni bajaring:

.. literalinclude:: ../examples/speaker_notes.py

Servo
-----

Bitta pin, 3.3v va yerga (ground) ulangan servo motor.

.. image:: /images/servo.svg
    :alt: Servo motorga ulangan Raspberry Pi Pico diagrammasi

Servoni minimal, o'rta va maksimal pozitsiyalariga o'tkazing.

.. literalinclude:: ../examples/servo_move.py

Servoni minimal va maksimal pozitsiyalari orasida puls qiling.

.. literalinclude:: ../examples/servo_pulse.py

Servoni minimaldan maksimal pozitsiyaga 100 ta qadam bilan asta-sekin o'tkazing.

.. literalinclude:: ../examples/servo_sweep.py

Motor
-----

Ikkita pin (old va orqa) va motor kontroller platasi orqali ulangan motorni boshqarish:

.. literalinclude:: ../examples/motor_move.py

Robot rover
-----------

Oddiy ikki g'ildirakli robot rover yasang.

.. image:: /images/robot_bb.svg
    :alt: Batareya paketi bilan ishlaydigan motor kontroller platasi orqali ikkita motorga ulangan Raspberry Pi Pico diagrammasi.

Roverni 1 soniya davomida oldinga yurgazing va to'xtating:

.. literalinclude:: ../examples/robot_rover_forward.py

Roverni (taxminan) kvadrat bo'ylab harakatlantiring:

.. literalinclude:: ../examples/robot_rover_square.py

Stepper motor (Stepper motor)
-----------------------------

Drayver platasi (masalan, ULN2003) orqali ulangan stepper motorni boshqarish.

Analog soat
~~~~~~~~~~~

Uzluksiz ishlaydigan analog soatning soniya milini yaratish:

.. literalinclude:: ../examples/stepper_analog_clock.py

Avtomatik pardalar
~~~~~~~~~~~~~~~~~~

Vaqtga asoslangan parda boshqaruvchisi:

.. literalinclude:: ../examples/stepper_automatic_blinds.py

Ichki harorat sensori
---------------------

Raspberry Pi Pico-ning ichki haroratini Selsiy darajasida tekshiring:

.. literalinclude:: ../examples/pico_temperature.py

Ultratovushli masofa sensori
----------------------------

Ultratovushli masofa sensoridan (HC-SR04) masofani santimetrda oling:

.. image:: /images/distance_sensor_bb.svg
    :alt: HC-SR04 masofa sensoriga ulangan Raspberry Pi Pico diagrammasi.

.. literalinclude:: ../examples/ultrasonic_distance_sensor.py

LCD displey
-----------

I2C shinasi va PCF8574 I2C adapteridan foydalanib LiquidCrystal displeylarida (LCD) belgilarni chop eting.

.. image:: /images/i2c_lcd.png
    :alt: I2C shinasi orqali 16x2 belgili LCD displeyga ulangan Raspberry Pi Pico diagrammasi.

.. literalinclude:: ../examples/i2c_lcd.py

Faqat GPIO pinlaridan foydalanib LiquidCrystal displeylarida (LCD) belgilarni chop eting.

.. image:: /images/lcd.png
    :alt: 16x2 belgili LCD displeyga ulangan Raspberry Pi Pico diagrammasi.

.. literalinclude:: ../examples/lcd.py
