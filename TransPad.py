import logging.config

import rumps

from trans_pad.config import config
from trans_pad.trans_pad import main
from trans_pad.sentry import init_sentry

LOGGING = {
    'version': 1,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)s[%(levelname)s] %(message)s'
        },
        'NSLog': {
            'format': '%(name)s[%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': 'DEBUG',
        },
        'NSLog': {
            'class': 'trans_pad.helpers.LoggingNSLogHandler',
            'formatter': 'NSLog',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'trans_pad': {
            'handlers': ['console', 'NSLog'],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console', 'NSLog'],
        'propagate': True,
        'level': 'DEBUG',
    },
}

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING)
    init_sentry(
        dsn=config.Support.sentry_dsn,
        app_name='TransPad',
    )
    rumps.debug_mode(True)

    main()
