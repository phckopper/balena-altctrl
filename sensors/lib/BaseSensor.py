class HardwareSensor(object):
    def __init__(self, data):
        self._channels = {}
        self._setup_channels()

    def _setup_channels(self):
        raise NotImplementedError

    def _read_from_device(self):
        raise NotImplementedError

    def get_readings(self):
        self._read_from_device()
        return self._channels

    def _register_channel(self, name, channel):
        self._channels[name] = channel
    
    def _set_channel(self, name, value):
        self._channels[name].set_value(value)

class I2CSensor(HardwareSensor):
    def __init__(self, data, address):
        self.address = address
        super().__init__(data)

class BaseChannel(object):
    value = None
    
class BinaryChannel(BaseChannel):
    def __init__(self):
        super().__init__()
        self.type = "binary"
    def set_value(self, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise ValueError("BinaryChannel must receive bools only!")

class RealChannel(BaseChannel):
    ON_OVF_CAP = 0
    ON_OVF_ERR = 1

    def __init__(self, min, max, unit, overflow_behavior=ON_OVF_CAP):
        self.min = min
        self.max = max
        self.unit = unit
        self.overflow_behavior = overflow_behavior
        self.type = "real"
    
    def set_value(self, value):
        if (value > self.max or value < self.min) and self.overflow_behavior == self.ON_OVF_ERR:
            raise ValueError(f"Value {value} is not between {self.min} (min) and {self.max} (max)!")
        else:
            self.value = min(self.max, max(self.min, value))
        
