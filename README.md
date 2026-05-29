# Raspberry Pi to Arduino Communication

Serial communication between Raspberry Pi and Arduino using HC-SR04 ultrasonic sensor and SG90 servo motor. Object detected within 30cm triggers servo open/close.

## Architecture

```
HC-SR04 (Ultrasonic) ──→ Arduino UNO ──→ Serial USB ──→ Raspberry Pi
                              │
                              └──→ SG90 Servo (open/close)
```

## Features

- Ultrasonic distance measurement every 1 second
- Servo actuation based on 30cm threshold (open/close)
- Serial data transmission from Arduino to Raspberry Pi
- Graceful SIGINT handling in Python script
- Configurable threshold, baud rate, and serial port

## Tech Stack

- Arduino C++ (Servo library)
- Python 3 (pyserial)
- HC-SR04 ultrasonic sensor, SG90 servo motor

## Project Structure

```
rpi_to_arduino/
├── arduino.ino     # Arduino sketch (sensor + servo + serial)
├── rpi.py          # Python serial reader
└── README.md
```

## Hardware Wiring

| Component | Arduino Pin |
|-----------|-------------|
| HC-SR04 Trig | Pin 9 |
| HC-SR04 Echo | Pin 10 |
| SG90 Servo | Pin 6 |

## Setup

### Arduino

1. Open `arduino.ino` in Arduino IDE
2. Upload to Arduino UNO
3. Connect HC-SR04 and servo per wiring table

### Raspberry Pi

```bash
pip install pyserial
python3 rpi.py
```

## Configuration

In `rpi.py`:
- `SERIAL_PORT`: defaults to `/dev/ttyUSB0`
- `BAUD_RATE`: defaults to `9600`
- `THRESHOLD_CM`: defaults to `30`
