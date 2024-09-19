class Validate:
    def input(self, prompt, validate, pattern=None):
        while True:
            func = getattr(self, validate, self.default)
            # noinspection PyArgumentList
            value = func(input(f"{prompt}: "), pattern)
            if value is not False:
                return value

    def default(self, info, pattern=None):
        return info

    def int(self, info, pattern=None):
        try:
            int_value = int(info)
            if pattern is not None:
                if pattern[0] <= int_value <= pattern[1]:
                    return int_value
                else:
                    DisplayInfo().warning(f"{info} 不在{pattern[0]}-{pattern[1]}之间")
                    return False
            else:
                return int_value
        except ValueError:
            DisplayInfo().warning(f"{info} 不是一个整数")
            return False

    def float(self, info, pattern=None):
        try:
            float_value = float(info)
            if pattern is not None:
                if pattern[0] <= float_value <= pattern[1]:
                    return float_value
                else:
                    DisplayInfo().warning(f"{info} 不在{pattern[0]}-{pattern[1]}之间")
                    return False
            else:
                return float_value
        except ValueError:
            DisplayInfo().warning(f"{info} 不是一个数")
            return False

    def date(self, info, pattern=None):
        from datetime import datetime
        date_format = "%Y-%m-%d"
        try:
            date_value = datetime.strptime(info, date_format)
            return date_value
        except ValueError:
            DisplayInfo().warning(f"请输入格式为 {date_format} 的日期")
            return False

class DisplayInfo:
    def pprint(self, info):
        print(f"*** {info}")

    def warning(self, info):
        self.pprint(f"WARNING: {info}")

    def notice(self, info):
        self.pprint(f"NOTICE: {info}")
