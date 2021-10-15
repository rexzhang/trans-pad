rm -rf .eggs build dist
pip install -U pip wheel
pip install -U -r requirements.txt

python build.py gettext
python setup.py py2app

python build.py popclip

rm *.dmg
# create-dmg --no-internet-enable "TransPad.dmg" "dist"
create-dmg "TransPad.dmg" "dist"
