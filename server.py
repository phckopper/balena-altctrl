#!/usr/bin/env python

import asyncio
import json
import websockets


class DataPoller(object):
    INTERVAL_1HZ  = 1
    INTERVAL_30HZ = (1/30.)
    INTERVAL_60HZ = (1/60.)

    def __init__(self, rate=INTERVAL_30HZ):
        self.rate = rate
        self.sensors = {}
        self._init_sensors()

    def _init_sensors(self):
        import sensors
        print("Initializing sensors...")
        for name, obj in sensors.__dict__.items():
            if obj is not sensors.HardwareSensor and isinstance(obj, type) and issubclass(obj, sensors.HardwareSensor):
                try:
                    self.sensors[name] = obj({})
                    print(f"Initialized {name} successfully!")
                except:
                    print(f"Failed to initialize {name} module!")
        print("Sensors initialized!")

    async def get_sensor_data(self):
        data = {}
        for s in self.sensors:
            data[s] = self.sensors[s].get_readings()
        await asyncio.sleep(self.rate)
        return data

async def handler(websocket):
    poller = DataPoller()
    while True:
        await websocket.send(json.dumps(await poller.get_sensor_data(), default=vars))

async def main():
    async with websockets.serve(handler, "0.0.0.0", 34567):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())