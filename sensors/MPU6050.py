from .lib.BaseSensor import I2CSensor, RealChannel

import board
import adafruit_mpu6050

class MPU6050(I2CSensor):
    ADDRESS = 0x68
    def __init__(self, data):
        super().__init__(data, self.ADDRESS)
        i2c = board.I2C()  # uses board.SCL and board.SDA
        self.mpu = adafruit_mpu6050.MPU6050(i2c)
        self.mpu.accelerometer_range = adafruit_mpu6050.Range.RANGE_8_G
        self.mpu.gyro_range = adafruit_mpu6050.GyroRange.RANGE_250_DPS

    def _setup_channels(self):
        self._register_channel("acc_x", RealChannel(-10*8, 10*8, "m/s^2")) # 8G, g = 10m/s^2
        self._register_channel("acc_y", RealChannel(-10*8, 10*8, "m/s^2"))
        self._register_channel("acc_z", RealChannel(-10*8, 10*8, "m/s^2"))

        self._register_channel("gyro_x", RealChannel(-250, 250, "deg/s")) # +- 250 deg/s
        self._register_channel("gyro_y", RealChannel(-250, 250, "deg/s"))
        self._register_channel("gyro_z", RealChannel(-250, 250, "deg/s"))
        
    def _read_from_device(self):
        acc_x, acc_y, acc_z = self.mpu.acceleration
        gyro_x, gyro_y, gyro_z = self.mpu.gyro
        self._set_channel("acc_x", acc_x)
        self._set_channel("acc_y", acc_y)
        self._set_channel("acc_z", acc_z)

        self._set_channel("gyro_x", gyro_x)
        self._set_channel("gyro_y", gyro_y)
        self._set_channel("gyro_z", gyro_z)