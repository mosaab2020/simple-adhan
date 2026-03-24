# simple-adhan
Simple script for getting adhan using the [AlAdhan api](https://aladhan.com/).
can be used with waybar.

![program gif](https://github.com/mosaab2020/simple-adhan/blob/main/gif/gif1.gif)

## Dependencies
you need the following installed:
[python3](https://www.python.org/)

## Installation

```bash
pip install simple-adhan
```

## Usage
- `--json`, `-j`: output json
- `--country COUNTRY`, `-C COUNTRY`: choose a country (default: SA)
- `--city CITY`, `-c CITY`: choose a city (default: Mecca)
- `--date`, `-d`: get the hijri date

## Run it

### Example:
```bash
simple-adhan --country "UK" --city "London"
```
or if you want to get the hijri date:

```bash
simple-adhan --country "UK" --city "London" --date
```

### Use it with waybar:
#### Make sure that simple-adhan is in your global PATH so waybar can access it.

```json
"custom/simple_adhan": {
    "exec": "simple-adhan --json --country COUNTRY --city CITY",
    "format": "{}",
    "format-alt": "{alt}",
    "interval": 60,
    "return-type": "json"
}
```
#### Customize it in the style.css file in waybar config:
```css
#custom-simple_adhan {
    /* add your styles here */
}
```
