import random


class Event():
    def __init__(self, name=""):
        self.event_name = name

    def __str__(self):
        return self.event_name


class Accelerate(Event):
    def __init__(self, v):
        super().__init__("Accelerate")
        self.acc_value = v


class Continue(Event):
    def __init__(self):
        super().__init__("Continue")


class Decelerate(Event):
    def __init__(self, v):
        super().__init__("Decelerate")
        self.dec_value = v


class Turn_off(Event):
    def __init__(self):
        super().__init__("Turn_off")


class Turn_left(Event):
    def __init__(self, ang):
        super().__init__("Turn_left")
        self.ang_value = ang


class Turn_right(Event):
    def __init__(self, ang):
        super().__init__("Turn_right")
        self.ang_value = ang


class Deer_jump(Event):
    def __init__(self):
        super().__init__("Deer_jump")


class Police_control(Event):
    def __init__(self):
        super().__init__("Police_control")


class Environment():
    def __init__(self):
        self.number = 0
        self.event = Continue()

    def generate_event(self):
        self.number = int(random.random() * 3)
        if self.number == 0:
            self.event = Continue()
            return self.event

        elif self.number == 1:
            self.event = Deer_jump()
            return self.event

        else:
            self.event = Police_control()
            return self.event


class Car():
    def __init__(self):
        self.wheel_angle = 0
        self.speed = 0
        self.is_running = True

    def act(self, event):
        print("car acts on event:")
        print(event)

        if event.event_name == "Turn_off":
            self.stop_the_car()

        elif event.event_name == "Accelerate":
            self.speed += event.acc_value
            if self.speed > 100:
                self.accident()

        elif event.event_name == "Decelerate":
            if self.speed < event.dec_value:
                self.speed = 0
            else:
                self.speed -= event.dec_value

        elif event.event_name == "Turn_right":
            self.wheel_angle += event.ang_value

        elif event.event_name == "Turn_left":
            self.wheel_angle += event.ang_value

        elif event.event_name == "Continue":
            self.do_nothing()

        elif event.event_name == "Police_control":
            if self.speed <= 50:
                print("You had police control and you passed it")
            elif self.speed > 50:
                print("You had police contol you was driving to fat ang you got a ticket")
                print("Pay it as soon as possible")

        elif event.event_name == "Deer_jump":
            if self.speed <= 30:
                print("Deer jumped out but you were driving slowly and stopped the car")
            elif self.speed > 30:
                print("Deer jumped out you hit it and you crashed")
                self.accident()

    def stop_the_car(self):
        self.is_running = False
        print("You have turned off your car")

    def print_car_info(self):
        print("Status: Running, Current Speed: {} , Steering wheel angle: {}\n".format(self.speed, self.wheel_angle))

    def accident(self):
        self.is_running = False
        print("You had accident")

    def do_nothing(self):
        print("Nothing happens")


if __name__ == "__main__":
    car1 = Car()

    event_name = ""
    event = Event()

    print("You are starting your ride")
    try:
        print("Insert value of speed you want to accelerate to:")
        car1.act(Accelerate(int(input())))
    except:
        car1.act(Accelerate(int(input(25))))

    value = 0

    environment = Environment()

    while car1.is_running:
        print()
        car1.print_car_info()

        print("Here are possible actions:")
        print("Accelerate, Decelerate, Turn_off, Continue, Turn_left, Turn_right")
        print("Enter what do you want to do:")

        try:
            event_name = input()
        except:
            event = Continue()

        if event_name == "Accelerate":
            print("Insert value:")
            try:
                value = int(input())
            except:
                value = 0
            event = Accelerate(value)

        elif event_name == "Decelerate":
            print("Insert value:")
            try:
                value = int(input())
            except:
                value = 0
            event = Decelerate(value)

        elif event_name == "Turn_off":
            value = 0
            event = Turn_off()

        elif event_name == "Turn_left":
            print("Insert angle of steering you want to set:")
            try:
                value = -int(input())
            except:
                value = 0
            event = Turn_left(value)

        elif event_name == "Turn_right":
            print("Insert angle of steering you want to set:")
            try:
                value = int(input())
            except:
                value = 0
            event = Turn_right(value)
        else:
            value = 0
            event = Continue()

        car1.act(event)

        car1.act(environment.generate_event())
