from setuptools import setup

__project__ = 'picozero_rw'
__packages__ = ['picozero']
__desc__ = 'A beginner-friendly library for using common electronics components with the Raspberry Pi Pico.'
__version__ = '0.4.3'
__author__ = "Roboticsware"
__author_email__ = 'roboticsware_uz@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/RaspberryPiFoundation/picozero'
__keywords__ = [
    'raspberry',
    'pi',
    'pico',
    'electronics',
    'roboticsware'
]
__classifiers__ = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Programming Language :: Python :: Implementation :: MicroPython',
    ]
__long_description__ = """A beginner-friendly library for using common electronics components with the Raspberry Pi Pico.  
Roboticsware added some functionalities based on picozero of Raspberry Pi Foundation.

```python
from picozero import LED, Button

led = LED(1)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off
```

```python
from picozero import I2cLcd
from time import sleep

lcd = I2cLcd(27, 26) # LCD 16x2, sda=27, scl=26

lcd.putstr('Hello World')
sleep(1)
lcd.move_to(0, 1)
lcd.putstr('Hello Roboticsware')
```

Documentation is available at [picozero.readthedocs.io](https://picozero.readthedocs.io/en/latest/).
"""

setup(
    name=__project__,
    version=__version__,
    description=__desc__,
    long_description=__long_description__,
    long_description_content_type='text/markdown',
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    classifiers=__classifiers__,
    keywords=__keywords__,
    packages=__packages__,
)