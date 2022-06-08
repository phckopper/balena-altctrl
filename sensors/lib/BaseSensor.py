

class HardwareSensor(object):
    INTERVAL_1HZ  = 1
    INTERVAL_30HZ = (1/30.)
    INTERVAL_60HZ = (1/60.)

    def __init__(self, data, sampling_interval=INTERVAL_60HZ):
        self.sampling_interval = sampling_interval
        self._setup_channels()
        self.channels = {}

    def _setup_channels(self):
        raise NotImplemented()

    def get_readings(self):
        return self.channels

    def _register_channel(self, name, channel):
        self.channels[name] = channel

class BaseChannel(object):
    def __init__(self, name):
        self.name = name
    
class BinaryChannel(BaseChannel):
    pass

class RealChannel(BaseChannel):
    pass
