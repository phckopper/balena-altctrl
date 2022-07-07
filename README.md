# Balena Altctrl

---

This project is meant to be a hardware abstraction layer for developing alternative controllers with balena. It automatically detects sensors over I2C and publishes the data in real time through a websocket.

---

### Organization

Inside the `sensors` directory we have the base class for the sensors inside the `lib` directory. A general `HardwareSensor` class is provided for generic sensors. Right now, the only specialized class is `I2CSensor`.

By subclassing HardwareSensor and implementing the `_setup_channels` and `_read_from_device` methods, the server is able to automatically detect and publish the retrieved data.

The data can either be sent as a `BinaryChannel`, for things like buttons or switches, or as a `RealChannel`, for things like accelerometers and gyroscopes. The client can then map them to keystrokes and joystick/mouse movements, respectively.

After writing your class, you should register it on the `sensors/__init__.py` file so that it can be discovered by the server.

---

### Current sensor support:

- MPU6050 (accelerometer + gyroscope)
- PCF8574 (8-bit I2C GPIO expander)
- PCF8575 (16-bit I2C GPIO expander)
- PN532 (NFC Reader **WIP**)

---

### Client software

Once the server is running, you can use the [altctrl-pc](https://github.com/phckopper/altctrl-pc) software to map your sensors to virtual inputs on your computer!