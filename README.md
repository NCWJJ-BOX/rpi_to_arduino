# RPI to Arduino Communication

Project ทดสอบการเชื่อมต่อและรับส่งข้อมูลระหว่าง Raspberry Pi กับ Arduino ผ่าน Serial

## Hardware

- **Arduino UNO** (หรือ board ที่รองรับ)
- **HC-SR04** Ultrasonic Sensor (วัดระยะทาง)
- **Servo Motor** (SG90 หรืออื่นๆ)
- **Raspberry Pi** (เชื่อมต่อ via USB)

## Wiring

| Arduino Pin | Component |
|-------------|-----------|
| Pin 9       | HC-SR04 Trig |
| Pin 10      | HC-SR04 Echo |
| Pin 6       | Servo Signal |

## Circuit

```
HC-SR04 -> Arduino
---------------
VCC      -> 5V
GND      -> GND
Trig     -> Pin 9
Echo     -> Pin 10

Servo -> Arduino
---------------
VCC    -> 5V
GND    -> GND
Signal -> Pin 6
```

## How It Works

1. **Arduino** วัดระยะทางด้วย Ultrasonic Sensor ทุก 1 วินาที
2. ถ้าระยะ < 30 cm → Servo หมุนไป 90° (เปิด)
3. ถ้าระยะ >= 30 cm → Servo กลับไป 0° (ปิด)
4. Arduino ส่งค่าระยะทางไปที่ Raspberry Pi ผ่าน Serial

## Setup

### Arduino
1. เปิด Arduino IDE
2. เปิดไฟล์ `arduino.ino`
3. Upload ไปยัง Arduino

### Raspberry Pi
1. ติดตั้ง pyserial:
   ```bash
   pip install pyserial
   ```
2. รัน script:
   ```bash
   python3 rpi.py
   ```

## Configuration

แก้ไขค่าใน `rpi.py`:

```python
SERIAL_PORT = '/dev/ttyUSB0'    # ปรับตาม port จริง
BAUD_RATE = 9600
DISTANCE_THRESHOLD_CM = 30
```

หา serial port:
```bash
ls -l /dev/ttyUSB*
```

## Output

```
Connected to Arduino on /dev/ttyUSB0 at 9600 baud
Distance: 25 cm
  -> Servo: OPEN (distance < 30 cm)
Distance: 45 cm
  -> Servo: CLOSED (distance >= 30 cm)
```

## Troubleshooting

- **Permission denied**: เพิ่ม user เข้า group dialout
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- **ไม่เจอ port**: ตรวจสอบ USB connection หรือ ใช้ `/dev/ttyACM0`
