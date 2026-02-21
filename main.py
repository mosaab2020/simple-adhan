#!/usr/bin/env python3

import adhanapi
import json
import argparse


def format_adhan_list(adhans: list(adhanapi.Adhan)):
    formatted_adhan_list = []
    flag_c = ""

    for adhan in adhans:
        if adhan.time_passed() is True:
            flag_c = "✔"
        else:
            flag_c = " "

        formatted_adhan_list.append("%s %s at %s" % (flag_c, adhan.s_name, adhan.format_twelve_hour()))

    list_str = "\n".join(formatted_adhan_list)

    return list_str


def get_next_adhan(adhans: list(adhanapi.Adhan)):
    next_adhan = None

    for adhan in adhans:
        if adhan.time_passed() is False:
            next_adhan = adhan
            break

    if next_adhan is None:
        formatted_next_adhan = "━━━━━━"
    else:
        formatted_next_adhan = "%s %s" % (next_adhan.s_name, next_adhan.format_twelve_hour())

    return formatted_next_adhan


def main():
    parser = argparse.ArgumentParser(description="simple program to get the time of the next salah", color=False)
    parser.add_argument("-j", "--json", action="store_true", help="output json for waybar")
    parser.add_argument("-d", "--date", action="store_true", help="get hijri date")
    parser.add_argument("-C", "--country", help="choose a country (default: SA)")
    parser.add_argument("-c", "--city", help="choose a city (default: Mecca)")
    args = parser.parse_args()

    # print(args.country, args.city)

    if (args.country is None or args.city is None):
        args.country = "SA"
        args.city = "Mecca"

    # Example: (change the country and city name)
    prayer_client = adhanapi.PrayClient(country=args.country, city=args.city)

    if args.date:
        print("Date:", prayer_client.hijri_date)
    else:
        adhans = prayer_client.today_adhan_times()

        # get a formatted string of adhan times
        formatted_adhan_list = format_adhan_list(adhans)

        # get a formatted string of the next adhan time
        formatted_next_adhan = get_next_adhan(adhans)

        if args.json:
            print(json.dumps({
                "text": formatted_next_adhan,
                "tooltip": formatted_adhan_list,
                "alt": prayer_client.hijri_date  # the alt is for the date
            }))
        else:
            print(formatted_adhan_list)

    return


main()
