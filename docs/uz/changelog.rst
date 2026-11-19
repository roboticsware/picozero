O'zgarishlar tarixi
===================

.. currentmodule:: picozero
0.6.2 - 2026-5-3
---------------
+ Asl picozero repozitoriysidan birlashtirildi (Merge qilindi).

0.6.1 - 2025-11-28
-----------

+ Hujjatlar yangilandi

0.6.0 - 2025-11-26
-----------

+ Qadamli motorlar (stepper motorlar) uchun ``Stepper`` klassi joriy etildi
+ Kapasitiv sensorlar uchun ``TouchSensor`` klassi joriy etildi
+ Testlar va hujjatlar yangilandi
+ Boshqa kichik xatolar tuzatildi

0.5.2 - 2025-11-26
-----------

+ Qo'lda o'rnatish ko'rsatmalaridagi 404 xatolik tuzatildi

0.5.1 - 2025-11-24
-----------

+ Hujjatlardagi noto'g'ri misol tuzatildi

0.5.0 - 2025-10-31
-----------

+ PIR sensorlari uchun ``MotionSensor`` klassi joriy etildi

0.4.2 ... 0.4.5
---------------

+ ``I2cLcd`` klassi qo'shildi
+ Servo uchun ``move_to_degree`` API-si qo'shildi
+ AnalogOutput(ADC) uchun ``raw_value`` xususiyati qo'shildi
+ Hujjatlar tartibga solindi va kichik xatolar tuzatildi

0.4.1 - 2022-12-22
------------------

+ ``pinout()`` qo'shildi
+ ``DigitalInputDevice.when_deactivated`` dekoratori bilan bog'liq xato tuzatildi
+ Hujjatlar tartibga solindi va kichik xatolar tuzatildi

0.4.0 - 2022-11-18
------------------

+ ``Servo`` klassi qo'shildi
+ Hujjatlardagi xatolar tuzatildi

0.3.0 - 2022-08-12
------------------

+ ``Motor``, ``Robot`` va ``DistanceSensor`` klasslari qo'shildi.
+ Boshqa klasslar bilan mos kelishi uchun ``LED`` zavodining ``use_pwm`` parametri nomi ``pwm``-ga o'zgartirildi. **Eslatma:** Bu API-da o'zgarishlarga olib keladigan (breaking change) yangilanish. 
+ ``pwm`` ishlatilmaganda ``RGBLED`` bilan bog'liq muammo hal qilindi.
+ ``blink`` / ``pulse`` chastotasi ``0`` bo'lganda yuzaga keladigan traceback xatosi hal qilindi.
+ Boshqa kichik xatolar tuzatildi.
+ Hujjatlar yangilandi.

0.2.0 - 2022-06-29
------------------

+ Ichki LED uchun Pico W mosligi tuzatildi.

0.1.1 - 2022-06-08
------------------

+ Sinov paytida aniqlangan xatolar uchun kichik tuzatishlar.
+ Istisno (exception) xabarlariga kichik yaxshilanishlar kiritildi.
+ Speaker va PWMOutputDevice uchun yopish (close) metodlari qo'shildi.
+ Unit testlar qo'shildi.
+ ``RGBLED.color``-ga taxallus sifatida ``RGBLED.colour`` qo'shildi.

0.1.0 - 2022-04-08
------------------

+ Beta versiya chiqarildi.
+ Hujjatlar yangilandi.
+ Kichik xatolar tuzatildi va kod refaktoring qilindi.

0.0.2 - 2022-03-31
------------------

+ Xatolar tuzatildi va hujjatlar yangilandi.

0.0.1 - 2022-03-21
------------------

+ O'rnatish jarayonini sinab ko'rish uchun birinchi alfa versiya chiqarildi.
