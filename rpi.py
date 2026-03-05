import serial
import time
import sys
import signal

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
DISTANCE_THRESHOLD_CM = 30
READ_INTERVAL_SEC = 1


def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)


def read_distance(ser):
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode('utf-8').strip()
            return int(data)
        except (UnicodeDecodeError, ValueError):
            return None
    return None


def main():
    signal.signal(signal.SIGINT, signal_handler)

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to Arduino on {SERIAL_PORT} at {BAUD_RATE} baud")
        time.sleep(2)
    except serial.SerialException as e:
        print(f"Failed to connect: {e}")
        sys.exit(1)

    while True:
        distance = read_distance(ser)
        
        if distance is not None:
            print(f"Distance: {distance} cm")
            
            if distance < DISTANCE_THRESHOLD_CM:
                print(f"  -> Servo: OPEN (distance < {DISTANCE_THRESHOLD_CM} cm)")
            else:
                print(f"  -> Servo: CLOSED (distance >= {DISTANCE_THRESHOLD_CM} cm)")
        
        time.sleep(READ_INTERVAL_SEC)


if __name__ == '__main__':
    main()
