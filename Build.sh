rm -rf build dist
python setup.py py2app

python build.py

rm *.dmg
create-dmg \
  --no-internet-enable \
  "TransPad.dmg" "dist"
