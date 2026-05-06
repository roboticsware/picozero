개발
====

picozero를 빌드하고 배포하는 방법에 대한 안내입니다.

사전 요구 사항
--------------

picozero를 빌드하고 배포하려면 다음 의존성을 설치해야 합니다::

    pip3 install twine sphinx 

빌드
----

1. ``setup.py``, ``picozero/__init__.py``, 그리고 ``docs/conf.py`` 파일의 버전 번호를 업데이트합니다.

2. ``docs/changelog.rst`` 에 릴리스 내용을 추가합니다.

3. ``setup.py`` 를 실행하여 소스 배포판을 만듭니다::

    python3 setup.py sdist

4. PyPI에 업로드합니다::

    twine upload dist/*

5. 모든 변경 사항을 ``master`` 브랜치에 푸시합니다.

6. GitHub에서 `릴리스 <https://github.com/roboticsware/picozero/releases>`_ 를 생성하고 ``picozero-#-#-#.tar.gz`` 소스 파일을 릴리스에 업로드합니다.

문서
----

문서 사이트는 Sphinx를 사용하여 구축되었습니다. 

다음 명령으로 sphinx를 설치합니다::

    pip3 install sphinx

문서 빌드를 테스트하려면 docs 디렉토리에서 다음 명령을 실행하십시오::

    $ ./make html

웹사이트는 docs/_build/html 디렉토리에 생성됩니다.

문서는 `picozero-rw.readthedocs.io`_에서 확인할 수 있으며, GitHub에 푸시할 때 자동으로 빌드 및 배포됩니다.

.. _picozero-rw.readthedocs.io: https://picozero-rw.readthedocs.io

테스트
------

테스트는 Raspberry Pi Pico에서 실행되도록 설계되었습니다.

1. `picozero <https://pypi.org/project/picozero/>`_ 패키지를 설치합니다.

2. `micropython-unittest <https://pypi.org/project/micropython-unittest/>`_ 패키지를 설치합니다.

3. ``test_picozero.py`` 파일을 Pico로 복사합니다.

4. ``test_picozero.py`` 파일을 실행합니다.

테스트가 실패할 경우 상세한 에러 메시지를 확인하는 것이 도움이 됩니다. 에러 메시지를 보려면 Pico의 ``lib/unittest.py`` 파일을 수정해야 합니다.

``run_class`` 함수에서 다음 코드를 찾으십시오::

    # Uncomment to investigate failure in detail
    #raise

``raise`` 의 주석을 해제합니다::

    # Uncomment to investigate failure in detail
    raise
