# TransPad

## Requirements

### Basic

- macOS 10.12(Sierra)+

### Development

- Python 3.10

## Building for Development

### Build

```shell
python build.py dev
```

### Run it

```shell
./dist/TransPad.app/Contents/MacOS/TransPad
```

## Building for Deployment

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
