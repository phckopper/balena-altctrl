from .lib.BaseSensor import HardwareSensor, RealChannel

class MPU6050(HardwareSensor):
    def __init__(self, data):
        super().__init__(data, HardwareSensor.INTERVAL_60HZ)

    def _setup_channels(self):
        self._register_channel(RealChannel("acc_x"))
        self._register_channel(RealChannel("acc_y"))
        self._register_channel(RealChannel("acc_z"))

        self._register_channel(RealChannel("gyro_x"))
        self._register_channel(RealChannel("gyro_y"))
        self._register_channel(RealChannel("gyro_z"))
        
        