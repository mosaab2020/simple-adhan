#!/usr/bin/env python3

import aladhan
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description="simple program to get the time of the next salah", color=False)
    parser.add_argument("-j", "--json", action="store_true", help="output json")
    args = parser.parse_args()

    try:
        # Ex:
        # location = aladhan.City("London", "GB")
        location = aladhan.City("", "")
        client = aladhan.Client(location)
        adhans = client.get_today_times()
    except Exception as e:
        print("Can't get time:", e)
        exit(1)

    tooltip_list = []
    flag_c = ""

    for adhan in adhans:
        if adhan.is_passed() is True:
            flag_c = "✔"
        else:
            flag_c = " "

        tooltip_list.append("%s %s at %s" % (flag_c, adhan.get_en_name(), adhan.readable_timing(show_date=False)))

    next_adhan = None

    for adhan in adhans:
        if adhan.is_passed() is False:
            next_adhan = adhan
            break

    if next_adhan is None:
        text = "------"
    else:
        text = "%s %s" % (next_adhan.get_en_name(), next_adhan.readable_timing(show_date=False))

    tooltip = "\n".join(tooltip_list)

    if args.json:
        print(json.dumps({
            "text": text,
            "tooltip": tooltip,
        }))
    else:
        print(tooltip)


main()

