from datetime import datetime


# CamelCase
# UpperCamelCase
# PascalCase
from typing import Union


class TimeHelper:

    # def __init__(self):
    #     self.MINUTE_SECONDS = 60
    #     self.HOUR_MINUTES = 60
    #     self.HOUR_SECONDS = self.MINUTE_SECONDS * self.HOUR_MINUTES

    # UPPER_SNAKE_CASE
    MINUTE_SECONDS = 60
    HOUR_MINUTES = 60
    HOUR_SECONDS = MINUTE_SECONDS * HOUR_MINUTES

    @classmethod
    def happened_in_last_hours(cls, x_hours: int, timestamp: Union[int, float]) -> bool:
        # print("class method called", cls)
        now = datetime.now()
        now_timestamp = now.timestamp()
        diff_seconds = now_timestamp - timestamp
        time_seconds = x_hours * cls.HOUR_SECONDS
        return diff_seconds < time_seconds


def main():
    th = TimeHelper()
    print(th.happened_in_last_hours(2, datetime.now().timestamp()))
    print(TimeHelper.happened_in_last_hours(2, datetime.now().timestamp()))


if __name__ == "__main__":
    main()
