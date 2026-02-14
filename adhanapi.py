from requests import exceptions
from requests_cache import CachedSession
from sys import stderr
from datetime import datetime, timedelta


URL = "https://api.aladhan.com/v1/timingsByCity"
TIMES_LIST = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]


class Adhan:
    def __init__(self, s_name: str, s_time: str):
        self.s_name = s_name
        self.s_time = s_time
        return

    # return true if the salah passed its time
    def time_passed(self):
        s_time_sec = sum(i * int(t) for i, t in zip([3600, 60], self.s_time.split(":")))

        today = datetime.today()
        time_now = (today.hour * 3600) + (today.minute * 60) + today.second

        if time_now >= s_time_sec:
            return True
        else:
            return False

    # return a 12-hour format time
    def format_twelve_hour(self):
        prefix = " (AM) "
        s_time_12 = self.s_time.split(":")

        time12 = int(s_time_12[0])
        if time12 >= 12:
            if time12 != 12:
                time12 = time12 - 12
            prefix = " (PM) "

        s_time_12[0] = str(time12)

        return ":".join(s_time_12) + prefix


class PrayClient:
    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city
        self.today = datetime.today()
        self.expire = (self.today + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        self.session = CachedSession("pray_times", use_cache_dir=True, expire_after=self.expire)
        self.data = None
        return

    def today_adhan_times(self):
        try:
            parameters = {"date": self.today.strftime("%Y-%m-%d"), "country": self.country, "city": self.city}
            response = self.session.get(URL, params=parameters)

            response.raise_for_status()

            self.data = response.json()

            # print("URL:", response.url)
            # print("Status:", response.status_code)
            # print(data["data"]["timings"])

            list = []
            for s_name, s_time in self.data["data"]["timings"].items():
                if s_name in TIMES_LIST:
                    list.append(Adhan(s_name, s_time))

            return list
        except exceptions.RequestException:
            error_data = response.json()["data"]
            print("Request error:", error_data, file=stderr)
            exit(1)

    # def get_sunrise(self):
    #     if self.data is None:
    #         return
    #     for s_name, s_time in self.data["data"]["timings"]:
    #         if s_name == "Sunrise":
    #             pass
