from .lib.BaseSensor import I2CSensor, BinaryChannel

import board
from adafruit_bus_device.i2c_device import I2CDevice

class PCF8575(I2CSensor):
    ADDRESS = 0x20 # read address

    def __init__(self, data):
        super().__init__(data, self.ADDRESS)
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.device = I2CDevice(i2c, self.ADDRESS)
        self.device.write(bytes([0xff, 0xff])) # enable pull-up on all pins
        self._setup_channels()

    def _setup_channels(self):
        for x in range(16):
            self._register_channel(f"D{x}", BinaryChannel())
        

    def _read_from_device(self):
        data = bytearray(2)
        self.device.readinto(data)

        for x in range(8):
            self._set_channel(f"D{x}", bool((data[0] >> x) & 1))

        for x in range(8):
            self._set_channel(f"D{x+8}", bool((data[1] >> x) & 1))