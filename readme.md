### Overview

Create virtual env
```bash
pip3 install virtualenv
python3 -m venv venv
```

Active virtual env:
```
source venv/bin/activate
```
Download libs
```
pip install -r requirement.txt
```

### Debug project

To debug project, run this command:
```
python3 main.py
```

### Package project

Package project 
```
pyinstaller --onefile --windowed --icon=static/icon.ico main.py
```

Note: to include data file (.json file) into your executable program, edit `main.spec`
```
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('yaml_templates.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
```
Then rebuild your app
```
pyinstaller main.spec
```

Finally, run command
```terminal
dist/main
```


