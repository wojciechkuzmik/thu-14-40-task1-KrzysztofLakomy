
#Possible events: Turn_off , Acceleration, Deceleration, Rotate_right, Rotate_left
    
class Car():
    def __init__(self):
        self.wheel_angle = 0
        self.speed = 0
        self.running = True


    def act(self, event):
        print("car acts on event:")
        print(event)

        if event[0] == "Turn_off":
            self.stop_the_car()

        if event[0] == "Acceleration":
            self.speed += int(event[1])
            if self.speed > 100:
                self.accident()

        if event[0] == "Deceleration":
            if self.speed < int(event[1]):
                self.speed = 0
            else:
                self.speed -= int(event[1])

        if event[0] == "Rotate_right":
            self.wheel_angle += int(event[1])

        if event[0] == "Rotate_left":
            self.wheel_angle -= int(event[1])

    def stop_the_car(self):
        self.running = False

    def print_car_info(self):
        print("Status: Launched, Current Speed: {} , Steering wheel angle: {}\n".format(self.speed,self.wheel_angle))

    def accident(self):
        self.running = False
        print("You have been speeding and you crashed")

car1 = Car()

Event = ["",0]

while car1.running:
    print()
    car1.print_car_info()

    print("Insert your event name:")
    Event[0] = input()

    print("Insert value:")
    Event[1] = input()

    car1.act(Event)



