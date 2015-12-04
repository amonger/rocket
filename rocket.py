#!/usr/bin/python

import usb
import time
import sys

class AbstractRocket:
    def get_name(self):
        return self.NAME

    def get_vendor_id(self):
        return self.VENDOR_ID

    def get_product_id(self):
        return self.PRODUCT_ID

    def up(self):
        return self.UP

    def down(self):
        return self.DOWN

    def left(self):
        return self.LEFT

    def left_up(self):
        return self.LEFT_UP

    def left_down(self):
        return self.LEFT_DOWN

    def left_slow(self):
        return self.LEFT_SLOW

    def right(self):
        return self.RIGHT

    def right_up(self):
        return self.RIGHT_UP

    def right_down(self):
        return self.RIGHT_DOWN

    def right_slow(self):
        return self.RIGHT_SLOW

    def stop(self):
        return self.STOP

class RocketManager:
    def __init__(self, rocket):
        self.rocket = rocket
        device_found = False
        for bus in usb.busses():
            for dev in bus.devices:
                if dev.idVendor == self.rocket.get_vendor_id() and dev.idProduct == self.rocket.get_product_id():
                    device_found = True
                    self.handle = dev.open()
                    print 'Device Primed: ' + self.rocket.get_name()

        if (device_found == False):
            print 'Device Not Found: ' + self.rocket.get_name()
            sys.exit(0)

    def issue_command(self, command):
        try:
            self.handle.controlMsg(0x21, 0x09, [command], 0x0200)
        except usb.USBError, e:
            pass

    def up(self):
        return self.issue_command(self.rocket.up())

    def down(self):
        return self.issue_command(self.rocket.down())

    def left(self):
        return self.issue_command(self.rocket.left())

    def left_up(self):
        return self.issue_command(self.rocket.left_up())

    def left_down(self):
        return self.issue_command(self.rocket.left_down())

    def left_slow(self):
        return self.issue_command(self.rocket.left_slow())

    def right(self):
        return self.issue_command(self.rocket.right())

    def right_up(self):
        return self.issue_command(self.rocket.right_up())

    def right_down(self):
        return self.issue_command(self.rocket.right_down())

    def right_slow(self):
        return self.issue_command(self.rocket.right_slow())

    def stop(self):
        return self.issue_command(self.rocket.stop())

class CircusRocket(AbstractRocket):
    NAME = "Circus Rocket"

    VENDOR_ID = 0x1941
    PRODUCT_ID = 0x8021

    UP = 1
    DOWN = 2
    LEFT = 4
    LEFT_UP = 5
    LEFT_DOWN = 6
    LEFT_SLOW = 7
    RIGHT = 8
    RIGHT_UP = 9
    RIGHT_DOWN = 10
    RIGHT_SLOW = 11
    STOP = 12

rocket = CircusRocket()
rocketManager = RocketManager(rocket)
rocketManager.up()
