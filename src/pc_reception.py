import serial
import time

# Open serial port for communication with the device
ser = serial.Serial('/dev/ttyUSB0', 2400)  # Replace '/dev/ttyUSB0' with the appropriate port name
received_data = b''  # Variable to store received data as bytes

# Wait until data is received
while ser.in_waiting == 0:
    pass

# Record start time for reception
start_time = time.time()

# Read data until receiving '$' (end marker)
while True:
    byte = ser.read(1)  # Read one byte at a time
    if byte == b'$':  # End marker received
        break
    received_data += byte  # Add byte ata buffer

# Record end time for reception
end_time = time.time()

# Calculate reception time
reception_time = end_time - start_time

# Calculate reception speed
data_size = len(received_data)  # Total number of bytes received
reception_speed = data_size / reception_time  # Bytes per second

print("Reception done")
print("Reception speed: {:.2f} bytes/second".format(reception_speed))

# Close serial port
ser.close()
