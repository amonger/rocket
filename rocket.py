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
                    print 'Device Assigned: ' + self.rocket.get_name()

        if (device_found == False):
            print 'Device Not Found: ' + self.rocket.get_name()
            sys.exit(0)

    def issue_command(self, command, command_name):
        try:
            print 'Issuing Command: ' + command_name
            self.handle.controlMsg(0x21, 0x09, [command], 0x0200)
        except usb.USBError, e:
            pass

        return self

    def up(self):
        return self.issue_command(self.rocket.up(), 'UP')

    def down(self):
        return self.issue_command(self.rocket.down(), 'DOWN')

    def left(self):
        return self.issue_command(self.rocket.left(), 'LEFT')

    def left_up(self):
        return self.issue_command(self.rocket.left_up(), 'LEFT UP')

    def left_down(self):
        return self.issue_command(self.rocket.left_down(), 'LEFT DOWN')

    def left_slow(self):
        return self.issue_command(self.rocket.left_slow(), 'LEFT SLOW')

    def right(self):
        return self.issue_command(self.rocket.right(), 'RIGHT')

    def right_up(self):
        return self.issue_command(self.rocket.right_up(), 'RIGHT UP')

    def right_down(self):
        return self.issue_command(self.rocket.right_down(), 'RIGHT DOWN')

    def right_slow(self):
        return self.issue_command(self.rocket.right_slow(), 'RIGHT SLOW')

    def stop(self):
        return self.issue_command(self.rocket.stop(), 'STOP')

    def sleep(self, timeout):
        time.sleep(timeout)
        return self

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
