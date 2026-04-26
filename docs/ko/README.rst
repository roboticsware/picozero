picozero-rw
===========

|pypibadge| |docsbadge|

Raspberry Pi Pico에서 일반적인 전자 부품을 쉽게 사용할 수 있도록 도와주는 초보자 친화적인 라이브러리입니다.

이 라이브러리는 `원래의 picozero 라이브러리 <https://github.com/RaspberryPiFoundation/picozero>`_ 를 포크한 것입니다.


.. code-block:: python

    from picozero import LED, Button

    led = LED(1)
    button = Button(2)

    button.when_pressed = led.on
    button.when_released = led.off

상태
----

베타 버전입니다. 버그와 이슈가 있을 수 있습니다. API 변경이 있을 수 있습니다. 시간이 지남에 따라 더 많은 장치가 추가될 예정입니다.

문서
----

문서는 `picozero-rw.readthedocs.io <https://picozero-rw.readthedocs.io>`_ 에서 확인할 수 있습니다:

- `설치 및 시작 가이드 <https://picozero-rw.readthedocs.io/en/latest/gettingstarted.html>`_
- `레시피 및 사용법 <https://picozero-rw.readthedocs.io/en/latest/recipes.html>`_
- `API <https://picozero-rw.readthedocs.io/en/latest/api.html>`_
- `예제 코드 <https://github.com/roboticsware/picozero/tree/master/docs/examples>`_

코드
----

코드와 프로젝트는 `github.com/roboticsware/picozero <https://github.com/roboticsware/picozero>`_ 에 있습니다.

이슈는 `github.com/roboticsware/picozero/issues <https://github.com/roboticsware/picozero/issues>`_ 에서 제기할 수 있습니다 (`기여하기 <https://picozero-rw.readthedocs.io/en/latest/contributing.html>`_ 참고).

최신 배포판은 `pypi.org/project/picozero-rw/ <https://pypi.org/project/picozero-rw/>`_ 에서 확인할 수 있습니다.

감사의 말
--------

picozero는 `gpiozero <https://gpiozero.readthedocs.io/en/stable/>`_ 에서 영감을 받았으며 (일부 기본 구조를 재사용함), Raspberry Pi Pico에 맞게 더 가볍고 정렬되도록 설계되었습니다. gpiozero 프로젝트에 기여해주신 모든 분들께 감사드립니다.

.. |pypibadge| image:: https://badge.fury.io/py/picozero-rw.svg
   :target: https://badge.fury.io/py/picozero-rw
   :alt: 최신 버전

.. |docsbadge| image:: https://readthedocs.org/projects/picozero-rw/badge/
   :target: https://readthedocs.org/projects/picozero-rw/
   :alt: 문서
