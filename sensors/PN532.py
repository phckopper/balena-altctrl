from .lib.BaseSensor import I2CSensor, BinaryChannel

import board
from adafruit_pn532.i2c import PN532_I2C

class PN532(I2CSensor):
    ADDRESS = 0x20 # read address

    def __init__(self, data):
        super().__init__(data, self.ADDRESS)
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.pn532 = PN532_I2C(i2c)
        ic, ver, rev, support = self.pn532.firmware_version
        print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
        self.pn532.SAM_configuration()
        self._setup_channels()

    def _setup_channels(self):
        for x in range(16):
            self._register_channel(f"NFC Card", BinaryChannel())
        

    def _read_from_device(self):
        uid = self.pn532.read_passive_target(timeout=0.05)
        self._set_channel(f"NFC Card", True if uid else False)