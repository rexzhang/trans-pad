from os.path import join
from zipfile import ZipFile

FILENAME_LIST = (
    ('popclip-extension/Config.plist', 'Config.plist'),
    'icon.png',
)


def build_pop_clip_extension():
    zip_filename = join('dist', 'TransPad.popclipextz')
    z = ZipFile(zip_filename, mode='w')

    for filename in FILENAME_LIST:
        if isinstance(filename, str):
            arcname = filename
        else:
            arcname = filename[1]
            filename = filename[0]

        z.write(filename, join('popclipext', arcname))

    z.close()
    print('Create:{} finished'.format(zip_filename))
    return


if __name__ == '__main__':
    build_pop_clip_extension()
