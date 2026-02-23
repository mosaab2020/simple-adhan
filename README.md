# simple-adhan
Simple script for getting adhan using the [AlAdhan api](https://aladhan.com/).
can be used with waybar.

## TESTED ONLY ON LINUX

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
- `--json`, `-j`: output json
- `--country COUNTRY`, `-C COUNTRY`: choose a country (default: SA)
- `--city CITY`, `-c CITY`: choose a city (default: Mecca)
- `--date`, `-d`: get the hijri date

## Run it

### Example:
```bash
./path/to/script/main.py --country "UK" --city "London"
```
or 

```bash
./path/to/script/main.py --country "UK" --city "London" --date
```

### Use it with waybar:
```json
"custom/simple_adhan": {
    "exec": "/path/to/script/main.py --json --country COUNTRY --city CITY",
    "format": "{}",
    "format-alt": "{alt}",
    "interval": 60, 
    "return-type": "json"
}
```

