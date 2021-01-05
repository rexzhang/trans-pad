"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['TransPad.py']
DATA_FILES = [
    'trans_pad/ui/preferences.xib',
]
OPTIONS = {
    'argv_emulation': True,

    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleIdentifier': 'com.rexzhang.TransPad',
        'LSUIElement': True,
        'NSServices': [
            {
                'NSMessage': 'translateTextService',
                'NSPortName': 'TransPadService',
                'NSMenuItem': {
                    'default': 'TransPad: Translate',
                    'Chinese': 'TransPad: 翻译文本',
                    'English': 'TransPad: Translate Text',
                },
                'NSSendTypes': ['NSStringPboardType'],
                # 'NSReturnTypes': ['NSStringPboardType'],
                'NSTimeout': '10000',  # 10 seconds
            },
        ],
    },
    # 'arch': 'universal2',
    # 'resources': [
    #       'img',
    # ],

    'packages': [
        # GUI
        'rumps',

        # 3rd
        'tree_struct_config',
        'googletrans',

        # support
        'sentry_sdk',
    ],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
