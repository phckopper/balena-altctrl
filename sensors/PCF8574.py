from .lib.BaseSensor import I2CSensor, BinaryChannel

import board
from adafruit_bus_device.i2c_device import I2CDevice

class PCF8574(I2CSensor):
    ADDRESS = 0x27 # read address

    def __init__(self, data):
        super().__init__(data, self.ADDRESS)
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.device = I2CDevice(i2c, self.ADDRESS)
        self.device.write(bytes([0xff])) # enable pull-up on all pins
        self._setup_channels()

    def _setup_channels(self):
        self._register_channel("D0", BinaryChannel())
        self._register_channel("D1", BinaryChannel())
        self._register_channel("D2", BinaryChannel())
        self._register_channel("D3", BinaryChannel())
        self._register_channel("D4", BinaryChannel())
        self._register_channel("D5", BinaryChannel())
        self._register_channel("D6", BinaryChannel())
        self._register_channel("D7", BinaryChannel())

    def _read_from_device(self):
        data = bytearray(1)
        self.device.readinto(data)

        for x in range(8):
            self._set_channel(f"D{x}", bool((data[0] >> x) & 1))