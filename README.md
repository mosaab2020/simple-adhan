# simple-adhan
Simple script for getting adhan using the [AlAdhan api](https://aladhan.readthedocs.io/_/downloads/en/latest/pdf/).

Can be used with waybar

```json
"custom/salah": {
    "format": "{}",
    "interval": 60,
    "escape": true,
    "return-type": "json",
    "exec": "/path/to/script/main.py --json"
},
```

