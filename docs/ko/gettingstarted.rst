.. picozero: a library for controlling Raspberry Pi Pico GPIO pins with MicroPython
..
.. SPDX short identifier: MIT

===============
시작하기
===============

Thonny를 사용하여 설치하기
=========================

요구 사항
---------

`Thonny Python IDE`_가 설치된 Windows, macOS 또는 Linux 컴퓨터가 필요합니다.

.. _Thonny Python IDE: https://thonny.org/

Thonny 설치 방법은 `Raspberry Pi Pico 소개 가이드`_에서 확인할 수 있습니다.

.. _Raspberry Pi Pico 소개 가이드: https://learning-admin.raspberrypi.org/en/projects/introduction-to-the-pico/2

Thonny가 설치되면 최신 MicroPython 펌웨어를 사용하고 있는지 확인해야 합니다. Raspberry Pi Pico MicroPython 펌웨어를 설치하거나 업데이트하는 방법에 대한 자세한 내용은 `Pico 가이드`_를 참조하십시오.

.. _Pico 가이드: https://learning-admin.raspberrypi.org/en/projects/introduction-to-the-pico/3

MicroPython 인터프리터 선택
--------------------------

화면 오른쪽 하단에서 원하는 옵션을 선택하여 Thonny에서 사용 중인 인터프리터를 변경할 수 있습니다. **MicroPython (Raspberry Pi Pico)**가 선택되어 있는지 확인하십시오.

.. image:: /images/thonny-switch-interpreter.jpg
    :alt: Thonny IDE 오른쪽 하단의 인터프리터 메뉴에서 MicroPython (Raspberry Pi Pico) 선택

Thonny에서 PyPI로부터 picozero 설치하기
--------------------------------------

Thonny 내에서 picozero를 설치하려면 **도구(Tools)** > **패키지 관리...(Manage packages...)**를 선택하십시오.

.. image:: /images/thonny-manage-packages.jpg
    :alt: Thonny의 도구 메뉴에서 패키지 관리 선택

PyPI에서 `picozero`를 검색하십시오.

.. image:: /images/thonny-packages-picozero.jpg
    :alt: Thonny의 패키지 관리 창의 검색 상자에 입력된 picozero

**설치(install)**를 클릭하여 패키지를 다운로드하십시오.

.. image:: /images/thonny-install-package.jpg
    :alt: 패키지 관리 창에 표시된 picozero 패키지 정보

수동 설치
========

picozero는 ``picozero.py`` 코드를 Raspberry Pi Pico에 복사하여 설치할 수 있습니다.

picozero `GitHub 저장소`_를 클론하거나 `picozero.py`_ 파일에서 코드를 복사하여 메인 컴퓨터에 저장하십시오.

.. _GitHub 저장소: https://github.com/roboticsware/picozero
.. _picozero.py: https://raw.githubusercontent.com/roboticsware/picozero/refs/heads/main/picozero/picozero.py

picozero.py라는 이름의 새 파일을 만들고 코드를 복사한 후 Raspberry Pi Pico에 저장하십시오.

Thonny를 사용하여 picozero.py 복사하기
------------------------------------

또는 Thonny 파일 관리자를 사용하여 ``picozero.py`` 파일을 Raspberry Pi Pico로 전송할 수 있습니다.

**보기(View)** 메뉴에서 **파일(Files)** 옵션에 체크되어 있는지 확인하십시오. 이렇게 하면 파일을 볼 수 있습니다.

.. image:: /images/thonny-view-files.jpg
    :alt: 보기 메뉴에서 선택된 파일 옵션

picozero `GitHub 저장소`_를 클론하거나 `picozero.py`_ 파일에서 코드를 복사하여 메인 컴퓨터에 저장하십시오.

.. _GitHub 저장소: https://github.com/roboticsware/picozero
.. _picozero.py: https://raw.githubusercontent.com/roboticsware/picozero/refs/heads/main/picozero/picozero.py

Thonny에서 클론한 디렉토리 또는 파일을 저장한 위치로 이동하여 ``picozero.py`` 파일을 찾으십시오.

.. image:: /images/thonny-navigate-downloads.jpg

파일을 오른쪽 버튼으로 클릭하고 **Upload to /** 옵션을 선택하십시오. Raspberry Pi Pico에 ``picozero.py`` 파일의 복사본이 표시되어야 합니다.

.. image:: /images/thonny-upload-files.jpg
    :alt: picozero.py 파일 메뉴에서 선택된 "Upload to /" 옵션
.. image:: /images/thonny-copy-picozero.jpg
    :alt: Raspberry Pi Pico 파일 뷰어에 표시된 picozero.py 파일

내장 LED를 제어하는 프로그램 작성하기
====================================

다음 코드는 내장 LED를 1초에 한 번씩 깜빡이게 합니다.::

    from picozero import pico_led
    from time import sleep

    while True:
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)

컴퓨터에서 프로그램 실행하기
--------------------------

컴퓨터에서 프로그램을 실행하도록 선택할 수 있습니다.

**현재 스크립트 실행(Run current script)** 버튼을 클릭하십시오.

.. image:: /images/run-current-script.jpg

**이 컴퓨터(This computer)**에 스크립트를 저장하도록 선택하고 파일 이름을 입력하십시오.

.. image:: /images/save-this-computer.png

Raspberry Pi Pico에서 프로그램 실행하기
--------------------------------------

Raspberry Pi Pico에서 프로그램을 실행하도록 선택할 수 있습니다.

**현재 스크립트 실행(Run current script)** 버튼을 클릭하십시오.

.. image:: /images/run-current-script.jpg

**Raspberry Pi Pico**에 스크립트를 저장하도록 선택하고 파일 이름을 입력하십시오.

.. image:: /images/save-this-raspberry-pi-pico.png

파일 이름을 ``main.py``로 정하면 Pico의 전원이 켜질 때 자동으로 실행됩니다.
