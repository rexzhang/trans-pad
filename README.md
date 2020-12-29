# TransPad

## Building for Development

Build

```shell
rm -rf build dist
python setup.py py2app -A
```

Copy `TransPad.app` to `/Applications`

## Building for deployment

```shell
brew install create-dmg
./Build.sh
```

#### Ref

- https://github.com/create-dmg/create-dmg
