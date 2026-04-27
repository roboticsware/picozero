import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# [추가] RTD 대시보드에서 설정할 환경 변수를 읽어옵니다 (기본값 'en')
# 이 변수는 나중에 RTD 프로젝트 설정에서 'ko', 'uz' 등으로 넣을 겁니다.
MY_DOC_LANG = os.environ.get('MY_DOC_LANG', 'en')

# Mock out certain modules
class Mock:
    __all__ = []
    def __init__(self, *args, **kw): pass
    def __call__(self, *args, **kw): return Mock()
    def __mul__(self, other): return Mock()
    def __and__(self, other): return Mock()
    def __bool__(self): return False
    def __nonzero__(self): return False
    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        else:
            return Mock()

sys.modules['machine'] = Mock()
sys.modules['micropython'] = Mock()

import time
setattr(time, 'ticks_ms', lambda x: None)
setattr(time, 'ticks_us', lambda x: None)

# -- Project information -----------------------------------------------------
project = 'picozero'
copyright = '2022, Raspberry Pi Foundation'
author = 'Raspberry Pi Foundation'
release = '0.4.5'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.viewcode', 
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']

# [수정] 언어별로 빌드할 때 다른 언어 폴더가 포함되지 않도록 제외 설정을 동적으로 변경합니다.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

if MY_DOC_LANG == 'ko':
    # 한국어 빌드 시: 영어 루트 파일들과 타 언어 폴더 제외
    exclude_patterns.extend(['uz/**', 'index.rst']) 
    language = 'ko'
elif MY_DOC_LANG == 'uz':
    # 우즈벡어 빌드 시: 영어 루트 파일들과 타 언어 폴더 제외
    exclude_patterns.extend(['ko/**', 'index.rst'])
    language = 'uz'
else:
    # 영어(기본) 빌드 시: 하위 언어 폴더들 제외
    exclude_patterns.extend(['ko/**', 'uz/**'])
    language = 'en'

# -- Options for HTML output -------------------------------------------------
if on_rtd:
    html_theme = 'sphinx_rtd_theme'
    html_sidebars = {
        '**': [
            'globaltoc.html',
            'relations.html',
            'searchbox.html',
        ],
    }
else:
    html_theme = 'alabaster'

html_static_path = ['_static']

# -- Autodoc configuration ------------------------------------------------
autodoc_member_order = 'groupwise'
autodoc_default_flags = ['members']