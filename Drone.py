import os
import time
os.system("sudo pigpiod")
time.sleep(1)
import pigpio
import getch


class Drone:
    def __init__(self):
        # Pin Setup
        self.thr = 26
        self.ail = 27
        self.ele = 22
        self.rudd = 21

        # Max Min Value
        self.thr_max = 2350
        self.thr_min = 1100
        self.rudd_max = 2000
        self.rudd_min = 1000
        self.ail_max = 2000
        self.ail_min = 1000
        self.ele_max = 2000
        self.ele_min = 1000

        ###  Initial Value
        self.thr_value = 1100
        self.rudd_value = 1500
        self.ail_value = 1500
        self.ele_value = 1500
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.thr, self.thr_value)
        self.pi.set_servo_pulsewidth(self.rudd, self.rudd_value)
        self.pi.set_servo_pulsewidth(self.ail, self.ail_value)
        self.pi.set_servo_pulsewidth(self.ele, self.ele_value)

    def calibrate(self):  # This is the auto calibration procedure of a normal ESC
        self.pi.set_servo_pulsewidth(self.thr, self.thr_min)
        print("Disconnect the battery and press Enter")
        inp = input()
        if inp == '':
            self.pi.set_servo_pulsewidth(self.thr, self.thr_max)
            print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
            inp = input()
            if inp == '':
                self.pi.set_servo_pulsewidth(self.thr, self.thr_min)
                print("Wierd eh! Special tone")
                time.sleep(2)
                print("Wait for it ....")
                time.sleep(2)
                print("Im working on it, DONT WORRY JUST WAIT.....")
                print("Done")

    def control(self, inp):
        # Throttel Setup
        if inp == "w":
            self.thr_value += 10
            self.pi.set_servo_pulsewidth(self.thr, self.thr_value)  # incrementing the speed like hell
            if self.thr_value >= self.thr_max:
                self.thr_value = 2350
            print("th speed = %d" % self.thr_value)

        elif inp == "s":
            self.thr_value -= 10
            self.pi.set_servo_pulsewidth(self.thr, self.thr_value)  # incrementing the speed like hell
            if self.thr_value <= self.thr_min:
                self.thr_value = 1100
            print("th speed = %d" % self.thr_value)

        # Rudder Setup
        elif inp == 'q':
            self.rudd_value += 10
            self.pi.set_servo_pulsewidth(self.rudd, self.rudd_value)
            print("Rudd_speed = %d" % self.rudd_value)
            if self.rudd_value >= self.rudd_max:
                self.rudd_value = 2000
        elif inp == 'e':
            self.rudd_value -= 10
            print("Rudd_speed = %d" % self.rudd_value)
            self.pi.set_servo_pulsewidth(self.rudd, self.rudd_value)
            if self.rudd_value <= self.rudd_min:
                self.rudd_value = 1000

        # Ailereon Setup (Left And Right)
        elif inp == 'a':
            self.ail_value += 10
            self.pi.set_servo_pulsewidth(self.ail, self.ail_value)
            print("Ail_speed = %d" % self.ail_value)
            if self.ail_value >= self.ail_max:
                self.rudd_value = 2000
        elif inp == 'd':
            self.ail_value -= 10
            print("Ail_speed = %d" % self.ail_value)
            self.pi.set_servo_pulsewidth(self.ail, self.ail_value)
            if self.ail_value <= self.ail_min:
                self.ail_value = 1000

        # Ele Setup (Front and Back)
        elif inp == 'r':
            self.ele_value += 10
            self.pi.set_servo_pulsewidth(self.ele, self.ele_value)
            print("Ele_speed = %d" % self.ele_value)
            if self.ele_value >= self.ele_max:
                self.ele_value = 2000
        elif inp == 'f':
            self.ele_value -= 10
            print("Ele_speed = %d" % self.ele_value)
            self.pi.set_servo_pulsewidth(self.ele, self.ele_value)
            if self.ele_value <= self.ele_min:
                self.ele_value = 1000

        # Arm Drone
        elif inp == "z":
            print("Drone Arm")
            self.pi.set_servo_pulsewidth(self.rudd, 1300)
            time.sleep(2)
            print("Drone Arm")
            self.pi.set_servo_pulsewidth(self.rudd, 1500)

        # Disarm Drone
        elif inp == "x":
            print("Drone Disarm")
            self.pi.set_servo_pulsewidth(self.rudd, 1720)
            time.sleep(2)
            self.pi.set_servo_pulsewidth(self.rudd, 1500)
            print("Drone Disarm")

        # Stop
        elif inp == 'v':
            print("Stop")
            self.pi.set_servo_pulsewidth(self.thr, self.thr_min)
            self.pi.set_servo_pulsewidth(self.rudd, self.rudd_value)
            self.pi.set_servo_pulsewidth(self.ail, self.ail_value)
            self.pi.set_servo_pulsewidth(self.ele, self.ele_value)

        else:
            self.pi.stop()
            exit()
