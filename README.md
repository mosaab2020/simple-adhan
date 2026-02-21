# simple-adhan
Simple script for getting adhan using the [AlAdhan api](https://aladhan.com/).
can be used with waybar.

## tested only on linux!

## Dependencies
you need the following installed:
[python3](https://www.python.org/),
[requests](https://pypi.org/project/requests/),
[requests-cache](https://requests-cache.readthedocs.io/en/stable/user_guide/installation.html),
argparse

## Installation
```bash
git clone https://github.com/mosaab2020/simple-adhan.git
cd simple-adhan
```

## Usage
- `--json` or `-j` to output json

## Run it
```bash
./path/to/script/main.py
```

### Use it with waybar:
```json
"custom/salah": {
    "format": "{}",
    "interval": 60,
    "escape": true,
    "return-type": "json",
    "exec": "/path/to/script/main.py --json"
},
```

