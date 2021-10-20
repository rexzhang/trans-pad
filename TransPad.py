import logging.config

import rumps

from trans_pad import __version__
from trans_pad.config import config
from trans_pad.helpers import i18n
from trans_pad.trans_pad import main
from trans_pad.sentry import init_sentry

LOGGING = {
    "version": 1,
    "formatters": {
        "console": {"format": "%(asctime)s %(name)s[%(levelname)s] %(message)s"},
        "NSLog": {"format": "%(name)s[%(levelname)s] %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "level": "DEBUG",
        },
        "NSLog": {
            "class": "trans_pad.helpers.LoggingNSLogHandler",
            "formatter": "NSLog",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "trans_pad": {
            "handlers": ["console", "NSLog"],
            "propagate": True,
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console", "NSLog"],
        "propagate": True,
        "level": "INFO",
    },
}

if __name__ == "__main__":
    debug = True
    # debug = False
    sentry_dsn = config.Support.sentry_dsn

    if debug:
        rumps.debug_mode(True)
        LOGGING["loggers"]["trans_pad"]["level"] = "DEBUG"
        LOGGING["root"]["level"] = "DEBUG"

    # logging
    logging.config.dictConfig(LOGGING)
    # sentry
    init_sentry(dsn=sentry_dsn, app_name="TransPad", app_version=__version__)
    # i18n
    i18n()

    main()
