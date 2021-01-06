# TransPad

## Requirements

### basic

- macOS 10.12(Sierra)+

### development

- Python 3.8

## Building for Development

Build

```shell
rm -rf .eggs build dist
python setup.py py2app -A
```

Copy `TransPad.app` to `/Applications`

## Building for deployment

### Install tools

brew

```shell
brew install create-dmg
```

or

```shell
git clone https://github.com/create-dmg/create-dmg.git
cd create-dmg
sudo make install
```

### Build it

```shell
./Build.sh
```

#### Ref

- https://github.com/create-dmg/create-dmg
