from datetime import datetime


# CamelCase
# UpperCamelCase
# PascalCase
class TimeHelper:

    # def __init__(self):
    #     self.MINUTE_SECONDS = 60
    #     self.HOUR_MINUTES = 60
    #     self.HOUR_SECONDS = self.MINUTE_SECONDS * self.HOUR_MINUTES

    # UPPER_SNAKE_CASE
    MINUTE_SECONDS = 60
    HOUR_MINUTES = 60
    HOUR_SECONDS = MINUTE_SECONDS * HOUR_MINUTES

    # def happened_in_last_hours(self, x_hours: int, timestamp: int) -> bool:
    #     print("method called", self)
    #     now = datetime.now()
    #     now_timestamp = now.timestamp()
    #     diff_seconds = now_timestamp - timestamp
    #     time_seconds = x_hours * self.HOUR_SECONDS
    #     return diff_seconds < time_seconds

    @classmethod
    def happened_in_last_hours(cls, x_hours: int, timestamp: int) -> bool:
        print("class method called", cls)
        now = datetime.now()
        now_timestamp = now.timestamp()
        diff_seconds = now_timestamp - timestamp
        time_seconds = x_hours * cls.HOUR_SECONDS
        return diff_seconds < time_seconds


def happened_in_last_hours(x_hours: int, timestamp: int) -> bool:
    now = datetime.now()
    now_timestamp = now.timestamp()
    diff_seconds = now_timestamp - timestamp
    time_seconds = x_hours * TimeHelper.HOUR_SECONDS
    return diff_seconds < time_seconds


def main():
    now = datetime.now()
    print(now)
    print(now.isoformat())
    print(now.timestamp())
    print(TimeHelper.happened_in_last_hours(1, int(now.timestamp())))
    # time_helper = TimeHelper()
    # print(time_helper.happened_in_last_hours(1, int(now.timestamp())))


if __name__ == '__main__':
    main()
