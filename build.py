import subprocess
from pathlib import Path
from zipfile import ZipFile

import click


@click.group()
def cli():
    pass


@cli.command('popclip', help='Build PopClip extension')
def cli_build_pop_clip_extension():
    filename_list = (
        ('popclip-extension/Config.plist', 'Config.plist'),
        'icon.png',
    )

    zip_filename = Path('dist').joinpath('TransPad.popclipextz')
    z = ZipFile(zip_filename, mode='w')

    for filename in filename_list:
        if isinstance(filename, str):
            arcname = filename
        else:
            arcname = filename[1]
            filename = filename[0]

        z.write(filename, Path('popclipext').joinpath(arcname))

    z.close()
    print('Create:{} finished'.format(zip_filename))
    return


LANGUAGES = (
    'en', 'fr', 'zh_CN'
)


def update_gettext():
    # Extract gettext message to TransPad.pot
    subprocess.run([
        'xgettext', '-v',
        '-f', Path('gettext').joinpath('source.txt'),
        '-o', Path('gettext').joinpath('TransPad.pot')
    ])

    # Update all *.po file from TransPad.pot
    for language in LANGUAGES:
        if language == 'en':
            continue

        subprocess.run([
            'msgmerge', '--update',
            Path('gettext').joinpath('{}.po'.format(language)),
            Path('gettext').joinpath('TransPad.pot')
        ])


@cli.command('update', help='Update gettext file: *.pot, *.po')
def cli_update_gettext():
    update_gettext()


def build_gettext():
    for language in LANGUAGES:
        Path('po').joinpath(
            language, 'LC_MESSAGES'
        ).mkdir(parents=True, exist_ok=True)
        subprocess.run([
            'msgfmt', 'gettext/{}.po'.format(language),
            '-o', 'po/{}/LC_MESSAGES/TransPad.mo'.format(language)]
        )


@cli.command('gettext', help='build gettext file: *.mo')
def cli_build_gettext():
    build_gettext()


def build_app_for_dev():
    subprocess.run(
        ['rm', '-rf', '.eggs', 'build', 'dist']
    )
    subprocess.run(
        ['python', 'setup.py', 'py2app', '-A']
    )


@cli.command('app', help='Build TransPad.app')
# @click.option('--release', default=False, help='build release app')
def cli_build_app():
    build_app_for_dev()


@cli.command('all', help='Build ALL')
def cli_build_all():
    build_gettext()
    build_app_for_dev()


if __name__ == '__main__':
    cli()
