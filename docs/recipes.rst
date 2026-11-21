Recipes
=======

The recipes provide examples of how you can use picozero.

Importing picozero
-------------------

.. currentmodule:: picozero

You will need add an `import` line to the top of your script to use picozero.

You can import just what you need, separating items with a comma ``,``::

    from picozero import pico_led, LED

Now you can use :obj:`~picozero.pico_led` and :class:`~picozero.LED` in your script::

    pico_led.on() # Turn on the LED on the Raspberry Pi Pico
    led = LED(14) # Control an LED connected to pin GP14 
    led.on()
 
Alternatively, the whole picozero library can be imported::

    import picozero

In this case, all references to picozero items must be prefixed::

    picozero.pico_led.on()
    led = picozero.LED(14)


Pico LED
--------

.. image:: /images/pico_led.svg
    :alt: A diagram of the Raspberry Pi Pico with a GP25 label attached to the onboard LED.

To turn on the LED on your Raspberry Pi Pico:

.. literalinclude:: examples/pico_led.py

Run your script to see the LED turn on.

Using the :obj:`pico_led` is equivalent to::

    pico_led = LED(25) 

You can use :obj:`pico_led` in the same way as external LEDs created using :class:`LED`.

Pin out
-------

You can output a *diagram* of the Raspberry Pi Pico which displays its pins and their numbers.

.. literalinclude:: examples/print_pinout.py

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

LEDs
------
 
.. image:: /images/pico_led_14_bb.svg
    :alt: A diagram of the Raspberry Pi Pico with a yellow LED connected to GP14 and GND.

You can control external LEDs with a Raspberry Pi Pico.

Flash
~~~~~

Turn an :class:`LED` on and off:

.. literalinclude:: examples/led_on_off.py

Toggle an :class:`LED` to turn it from on to off or off to on:

.. literalinclude:: examples/led_toggle.py

.. only:: html

   .. raw:: html

      <p>
        <a href="https://wokwi.com/projects/417606412375790593" target="_blank">
          🚀 Run in Wokwi Simulator
        </a>
      </p>

Alternatively, you can use the :meth:`~picozero.LED.blink` method.

.. literalinclude:: examples/led_blink.py

Brightness
~~~~~~~~~~

Set the brightness of an :class:`LED`:

.. literalinclude:: examples/led_brightness.py

Create a pulse effect:

.. literalinclude:: examples/led_pulse.py

Alternatively, you can use the :meth:`~picozero.LED.pulse` method.

.. literalinclude:: examples/led_pulse_method.py

Buttons
-------

You can connect buttons and switches to a Raspberry Pi Pico and detect when they are pressed. 

Check if a :class:`Button` is pressed:

.. literalinclude:: examples/button_is_pressed.py


Run a function every time a :class:`Button` is pressed:

.. literalinclude:: examples/button_function.py

.. note::

    The line ``button.when_pressed = led_on_off`` does not run the
    function ``led_on_off``, rather it creates a reference to the function to be
    called when the button is pressed. Accidental use of ``button.when_pressed
    = led_on_off()`` would set the ``when_pressed`` action to :data:`None` (the
    return value of this function), which would mean nothing happens when the
    button is pressed.

Turn the :obj:`pico_led` on when a :class:`Button` is pressed and off when it is released:

.. literalinclude:: examples/button_led.py

Touch sensor
------------

Detect touch using a capacitive touch sensor:

.. literalinclude:: examples/touch_sensor.py

Use callbacks to respond to touch events:

.. literalinclude:: examples/touch_sensor_callbacks.py

Motion sensor
-------------

Detect motion using a PIR (Passive Infrared) sensor:

.. literalinclude:: examples/motion_sensor.py

Use callbacks to respond to motion events:

.. literalinclude:: examples/motion_sensor_callbacks.py

RGB LEDs
--------

Set colours with an :class:`RGBLED`:

.. literalinclude:: examples/rgb_led.py

Use :meth:`~picozero.RGBLED.toggle` and :meth:`~picozero.RGBLED.invert`:

.. literalinclude:: examples/rgb_toggle_invert.py

Blink
~~~~~

Use :meth:`~picozero.RGBLED.blink` blink to change between colours. You can control which colours are used and how long the LED is set to each colour. The colour `(0, 0, 0)` represents off. 

You can control whether :meth:`~picozero.RGBLED.blink` runs a fixed number of times and whether it waits until it has finished or returns immediately so other code can run.

.. literalinclude:: examples/rgb_blink.py

Pulse
~~~~~

Use :meth:`~picozero.RGBLED.pulse` to gradually change the LED colour. The default will pulse between red and off, then green and off, then blue and off. 

.. literalinclude:: examples/rgb_pulse.py

Cycle
~~~~~

The default for :meth:`~picozero.RGBLED.cycle` is to cycle from red to green, then green to blue, then blue to red. 

.. literalinclude:: examples/rgb_cycle.py

Potentiometer
-------------

Print the value, voltage, and percent reported by a potentiometer:

.. literalinclude:: examples/potentiometer.py

.. note::

    In the Thonny Python editor, choose **View** > **Plotter** to plot the output of :meth:`print`. 

Use a potentiometer to control the brightness of an LED:

.. literalinclude:: examples/pot_led.py

Joystick
-------------

Joystick is similar to potentiometer so we can use the Pot class to control a joystick.

.. image:: /images/joystick.png
    :alt: A diagram of the Raspberry Pi Pico connected to a joystick

Move the joystick to its minimum, mid and maximum positions.

.. literalinclude:: examples/joystick.py

Buzzer
------

Control an active buzzer that plays a note when powered:

.. literalinclude:: examples/buzzer.py

Speaker
-------

Control a passive buzzer or speaker that can play different tones or frequencies:

.. literalinclude:: examples/speaker.py

Play a tune
~~~~~~~~~~~

Play a tune of note names and durations in beats: 

.. literalinclude:: examples/speaker_tune.py

Play individual notes
~~~~~~~~~~~~~~~~~~~~~

Play individual notes and control the timing or perform another action:

.. literalinclude:: examples/speaker_notes.py

Servo
-----

A servo motor (such as the SG-90) connected to a single GPIO pin (``GP1``), 5V (``VBUS``), and ground (``GND``):

.. note::
    Servo Power Wiring Note:

    - Servo motors draw large momentary currents during movement, so always power them from ``VBUS`` (USB 5V, Pin 40) instead of the Pico's 3.3V (``3V3``) pin to prevent brown-out resets.
    - If using multiple servos or high-load mechanisms, use an external 5V power supply with a shared common ground to ``GND``.

.. image:: /images/servo.svg
    :alt: A diagram of the Raspberry Pi Pico connected to a servo motor

Move the servo to its minimum, mid and maximum positions.

.. literalinclude:: examples/servo_move.py

Pulse the servo between its minumum and maximum position.

.. literalinclude:: examples/servo_pulse.py

Move the servo gradually from its minimum to maximum position in 100 increments.

.. literalinclude:: examples/servo_sweep.py

Motor
-----

Move a motor connected via two pins (forward and backward) and a motor controller board:

.. literalinclude:: examples/motor_move.py

Robot rover
-----------

Make a simple two-wheeled robot rover.

.. image:: /images/robot_bb.svg
    :alt: A diagram of the Raspberry Pi Pico connected to two motors via a motor controller board powered by a battery pack.

Move the rover forward for 1 second and stop:

.. literalinclude:: examples/robot_rover_forward.py

Move the rover (roughly) in a square:

.. literalinclude:: examples/robot_rover_square.py


Stepper motor
-------------

Control a 28BYJ-48 5V stepper motor connected via a driver board (e.g. ULN2003).

.. image:: /images/circuit_stepper.svg
    :alt: A diagram of the Raspberry Pi Pico connected to a stepper motor via a ULN2003 driver board

Basic rotation
~~~~~~~~~~~~~~

Basic clockwise and counter-clockwise rotation control:

.. literalinclude:: examples/stepper_basic.py

Analog clock
~~~~~~~~~~~~

Create a continuously-running analog clock second hand:

.. literalinclude:: examples/stepper_analog_clock.py

Automatic blinds
~~~~~~~~~~~~~~~~

Time-based blind controller:

.. literalinclude:: examples/stepper_automatic_blinds.py


Internal temperature sensor
---------------------------

Check the internal temperature of the Raspberry Pi Pico in degrees Celcius:

.. literalinclude:: examples/pico_temperature.py

Ultrasonic distance sensor
--------------------------

Get the distance in centimetres using a 3.3V-compatible ultrasonic distance sensor (**HC-SR04P** or **HC-SR04+** powered from ``3V3``):

.. warning::
    **5V Overvoltage Hazard (Legacy HC-SR04):** Standard 5V-only ``HC-SR04`` modules powered from ``VBUS`` (5V) output a **5V logic signal** on the ``ECHO`` pin. Raspberry Pi Pico (RP2040) GPIO pins operate at **3.3V** and are **not 5V-tolerant** — connecting a 5V ``ECHO`` pin directly to ``GP2`` can permanently damage the chip.

    - **Recommended:** Use a 3.3V–5V wide-voltage **HC-SR04P** (or **HC-SR04+**) powered from ``3V3`` (safe 3.3V ``ECHO``).
    - **If using a legacy 5V HC-SR04:** Step down the ``ECHO`` output to 3.3V using a **voltage divider** (e.g., ``1kΩ`` between ``ECHO`` and ``GP2``, plus ``2kΩ`` from ``GP2`` to ``GND``).

.. image:: /images/circuit_distance.svg
    :alt: A diagram of the Raspberry Pi Pico connected to an HC-SR04P 3.3V ultrasonic distance sensor.

.. literalinclude:: examples/ultrasonic_distance_sensor.py

OLED Display (I2C)
------------------

Display crisp text and graphics on a 0.96" or 1.3" **I2C OLED** module (``SSD1306`` or ``SH1106``). Unlike 5V character LCD backpacks, OLED modules operate natively at **3.3V** and wire directly to the Raspberry Pi Pico without a level shifter:

- Pass ``driver="sh1106"`` to ``OLED(...)`` if using a 1.3" SH1106 display instead of the default 0.96" SSD1306.

.. image:: /images/circuit_oled.svg
    :alt: A diagram of the Raspberry Pi Pico connected directly to a 3.3V I2C OLED display (SSD1306 or SH1106).

.. literalinclude:: examples/oled.py

LCD Display
-----------

Print characters on LiquidCrystal displays (16x2 LCD) by using the I2C bus with a PCF8574 I2C backpack:

.. warning::
    **Use a Logic Level Shifter (3.3V ⇄ 5V) for PCF8574:** Most 16x2 LCD modules require a **5V** supply (``VBUS``), and PCF8574 I2C backpacks include pull-up resistors to **5V**, which over-drive RP2040 GPIO pins (3.3V). Insert a bidirectional **I2C logic level shifter** (``LV ← 3V3``, ``HV ← VBUS 5V``) on ``SDA`` and ``SCL``, or switch to a **3.3V native I2C OLED** above.

.. image:: /images/circuit_i2c_lcd.svg
    :alt: A diagram of the Raspberry Pi Pico connected to a 5V 16x2 PCF8574 I2C LCD through a 3.3V to 5V bidirectional logic level shifter.

.. literalinclude:: examples/i2c_lcd.py

Print characters on LiquidCrystal displays (16x2 LCD) in 4-bit mode using GPIO pins directly:

.. note::
    **Write-Only Safety (RW → GND):** Although the HD44780 LCD module is powered from ``VBUS`` (5V), tying the ``RW`` (Read/Write) pin permanently to ``GND`` keeps the LCD in write-only mode so it never outputs 5V signals back into the Pico's 3.3V GPIO pins (``GP16`` to ``GP21``). Use a ``10kΩ`` potentiometer on ``V0`` for contrast and a ``220Ω`` series resistor on ``A`` for the backlight.

.. image:: /images/circuit_gpio_lcd.svg
    :alt: A diagram of the Raspberry Pi Pico connected to a 16x2 Character LCD in 4-bit GPIO mode with RW tied to GND.

.. literalinclude:: examples/lcd.py