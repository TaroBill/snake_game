import smbus
import math
from gpiozero import Button
from controller import IController

class MPUController(IController):
    def __init__(self) -> None:
        # Power management registers
        self.power_mgmt_1 = 0x6b
        self.bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
        self.address = 0x68       # This is the address value read via the i2cdetect command
        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
        
        self.button = Button(17)

    def read_byte(self, adr):
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self, adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(self, x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)
    
    def read_rotation(self):
        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f) 
        gyro_xout = self.read_word_2c(0x43)
        gyro_yout = self.read_word_2c(0x45)
        gyro_zout = self.read_word_2c(0x47)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0
        x_rot = self.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        y_rot = self.get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        return x_rot, y_rot
    
    def get_Direction(self) -> Direction:
        x_rot, y_rot = self.read_rotation()
        if x_rot > 20:
            return Direction.DOWN
        elif x_rot < -20:
            return Direction.UP
        elif y_rot > 20:
            return Direction.RIGHT
        elif y_rot < -20:
            return Direction.LEFT
        return None
    
    def start_button(self) -> bool:
        if self.button.value == 1:
            return True
        return False