#!/usr/bin/env python3

import adhanapi
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description="simple program to get the time of the next salah", color=False)
    parser.add_argument("-j", "--json", action="store_true", help="output json")
    args = parser.parse_args()

    # Example: (change the country and city name)
    prayer_client = adhanapi.PrayClient(country="UK", city="London")

    adhans = prayer_client.today_adhan_times()

    tooltip_list = []
    flag_c = ""

    for adhan in adhans:
        if adhan.time_passed() is True:
            flag_c = "✔"
        else:
            flag_c = " "

        tooltip_list.append("%s %s at %s" % (flag_c, adhan.s_name, adhan.format_twelve_hour()))

    next_adhan = None

    for adhan in adhans:
        if adhan.time_passed() is False:
            next_adhan = adhan
            break

    if next_adhan is None:
        text = "------"
    else:
        text = "%s %s" % (next_adhan.s_name, next_adhan.format_twelve_hour())

    tooltip = "\n".join(tooltip_list)

    if args.json:
        print(json.dumps({
            "text": text,
            "tooltip": tooltip,
        }))
    else:
        print(tooltip)


main()

