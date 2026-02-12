# simple-adhan
Simple script for getting adhan using the [AlAdhan api](https://aladhan.readthedocs.io/_/downloads/en/latest/pdf/).
can be used with waybar.

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

