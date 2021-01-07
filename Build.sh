rm -rf .eggs build dist
pip install -U pip wheel
pip install -U -r requirements.txt
python setup.py py2app

python build.py

rm *.dmg
create-dmg \
  --no-internet-enable \
  "TransPad.dmg" "dist"
