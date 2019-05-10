from Drone import Drone
import getch

drone = Drone()
while 1:
    drone.control(str(getch.getch()))
