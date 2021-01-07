import subprocess
from pathlib import Path
from zipfile import ZipFile

import click


@click.group()
def cli():
    pass


@cli.command('popclip', help='Only build PopClip extension')
def build_pop_clip_extension():
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


# @cli.command('gettext', help='Extract gettext message to TransPad.pot')
def gettext_extract_to_pot():
    subprocess.run(
        ['xgettext', '-v', '-f', 'gettext.txt', '-o', 'gettext/TransPad.pot'],
        # capture_output=True,
    )


def build_gettext():
    languages = (
        'en', 'zh_CN'
    )
    for language in languages:
        Path('po').joinpath(
            language, 'LC_MESSAGES'
        ).mkdir(parents=True, exist_ok=True)
        subprocess.run([
            'msgfmt', 'gettext/{}.po'.format(language),
            '-o', 'po/{}/LC_MESSAGES/TransPad.mo'.format(language)]
        )


@cli.command('gettext')
def build_gettext_cli():
    build_gettext()


def build_app_for_dev():
    subprocess.run(
        ['rm', '-rf', '.eggs', 'build', 'dist']
    )
    subprocess.run(
        ['python', 'setup.py', 'py2app', '-A']
    )


@cli.command('app', help='Only build TransPad.app')
# @click.option('--release', default=False, help='build release app')
def cli_build_app():
    build_app_for_dev()


@cli.command('all', help='Build ALL')
def build_all():
    build_gettext()
    build_app_for_dev()


if __name__ == '__main__':
    cli()
