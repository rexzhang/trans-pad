import logging

import sentry_sdk
from sentry_sdk import configure_scope
from sentry_sdk.integrations.excepthook import ExcepthookIntegration
from sentry_sdk.integrations.stdlib import StdlibIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.threading import ThreadingIntegration

INTEGRATIONS = [
    ExcepthookIntegration(always_run=True),
    StdlibIntegration(),
    ThreadingIntegration(propagate_hub=True),
    LoggingIntegration(
        level=logging.WARNING,  # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    ),
]


def get_mac_address() -> str:
    for name in ['eth0', 'en0']:
        try:
            import netifaces

            mac = netifaces.ifaddresses(name)[netifaces.AF_LINK][0]['addr']
            break

        except (ValueError, ImportError):
            mac = '00:00:00:00:00:00'
            continue

    return mac.upper()


def init_sentry(dsn: str, app_name: str = 'PyApp', app_version: str = '0.0.0'):
    sentry_sdk.init(
        dsn=dsn,
        environment='release',

        integrations=INTEGRATIONS,

        release='{}@{}'.format(app_name, app_version),

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,

        # before_send=auto_drop_event_for_rate_limit,
    )

    mac_address = get_mac_address()
    with configure_scope() as scope:
        scope.set_user({
            'id': mac_address
        })
