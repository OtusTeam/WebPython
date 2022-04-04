from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def on(self):
        raise NotImplementedError

    @abstractmethod
    def off(self):
        raise NotImplementedError


class LightBulb(Switchable):
    def on(self):
        print("light bulb turned on")

    def off(self):
        print("light bulb turned off")


# class WirelessMouse(Switchable, BatteryStatusInfo...):
class WirelessMouse(Switchable):
    def on(self):
        print("mouse turned on")

    def off(self):
        print("mouse turned off")


class PowerSwitch:
    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def toggle(self):
        if self.on:
            self.client.off()
            self.on = False
        else:
            self.client.on()
            self.on = True


def main():
    bulb = LightBulb()
    bulb.on()
    bulb.off()

    mouse = WirelessMouse()
    mouse.on()
    mouse.off()

    switch1 = PowerSwitch(bulb)
    switch1.toggle()
    switch1.toggle()
    switch1.toggle()
    switch1.toggle()

    switch2 = PowerSwitch(mouse)
    switch2.toggle()
    switch2.toggle()
    switch2.toggle()
    switch2.toggle()

    # Switchable()


if __name__ == '__main__':
    main()
