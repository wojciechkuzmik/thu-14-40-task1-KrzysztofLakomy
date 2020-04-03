During first laboratory we were doing task where we were supposed to write simulation of a car. We got an example how it should look like. Our car program was supposed to have some features like:
-	Working in infinite loop until we decide to break it
-	Every iteration print current car status: current speed, rotation of a steering wheel – difference between current angle and basic position which is non rotated steering wheel.  
-	React on variety of events like turning car left or right, accelerating and many more we wanted to create.
Our imagination was only limit. It was our decision how many events we wanted to create and how the car would act on them because main goal of this task was showing our best programming skills. We had limited time so we had to estimate how time-consuming is our idea to stay in the limit.
After first task I have learnt how generally write programs in python and got some tips how to write. First of them was that we should stick to PEP8. It is a guide how code written in python should look like. Using this guide we are able to write nice code which is clear to everyone reading it.
I also have learnt how to improve my program. I only created class representing the car. Now I know that good idea will be making events classes as well or even creating abstract class event and make every event inherit form this class event. It will make whole code neat and clear. 
Making environment class is also good. Environment is supposed to create events that happens to the car and car is sending back action on them to environment
