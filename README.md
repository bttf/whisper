# adnan's whisper implementation

pretty simple stuff

## steps to get running

1. setup venv

```
$ python -m venv venv
$ source venv/bin/activate
```

2. install packages

```
$ pip install -r requirements.txt
```

3. run script

```
$ python main.py ./test-video.mkv
```

## packaging with pyinstaller

after running steps 1. and 2. above, run the following:

```
$ pyinstaller main.spec
```

however, if that doesn't work, this is the original command:

```
pyinstaller --onefile --add-data './venv/lib/python3.11/site-packages/whisper/assets:whisper/assets' main.py
```
