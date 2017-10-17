# TinyMotorTests
Finding the fastest motors for a Tiny Whoop.

## Abstract
This work uses a Motion Capture system to analyse the thrust performace of micro quad motors in situ. Each quad was set up with throttle on a switch to test the instantaneous acceleration of each motor set.

## Introduction
There are many different choices when picking micro quad motors. 7mm or 6mm? What about those new 6x17mm motors? I set out to determine which motors actually provide the best thrust in situ, that is to say I didn't want to do a static thrust test on a workbench. There are several reasons for this, but mainly it's because given such small quads, there are a lot of unknown variables at play: inertia, air drag, losses due to battery droop, to name a few. All of these significantly change the flight style, and are difficult to quantify using a static thrust test setup.

## Experiments
The recording system used is an OptiTrack http://optitrack.com/ motion capture (Mo-cap) system, which I was kindly given access to by the Aeronautical Deptartment at The University of Sydney. This system can track reflective markers to an accuracy of <1mm and a rate of 120Hz, so its the best known testing environment for this experiment. To track the quadcopter, a single tracking 'dot' was placed on the quad, and the camera was removed to maintain weight. The dot and holder is 3.8 grams, and the camera 4.0 grams, so the weight difference is negligible.

<img src="https://github.com/azyner/TinyMotorTests/blob/master/images/QuadScale.jpg" width="300">

Each set of motors was given at least three punchouts, and at least two different batteries. The batteries used are mylipo.de HV PH2.0 packs, charged to only 4.2V (NOT HV charge). I tested four sets of motors: boldclash 0615 18000kv, micro-motor-warehouse: 0615 19000kv, 0617 25000kv, and 0716 17000kv. The 0716 and boldclash motors were fresh, the other two had about an hour of flight time. The FC used is a BeeBrain FC 1.2, with P2.0 plug. The same FC was used for all the motors. Frames used are 0617 Cockroach, 0716 Beta65, and 0615 Eachine E010S (The white one). Props used are the standard whoop props, cut to 2 blade for all tests.

For each test, the quad was placed on the ground, and a switch throttle was used. I have data for the entire climb, and I compare velocities at 3m of altitude. After 3 meters I had to kill throttle to avoid hitting the ceiling. The single best recording is compared between motors, where best is defined as greatest speed at 3m altitude.

<img src="https://github.com/azyner/TinyMotorTests/blob/master/images/ThrustTest.gif" width="300">

## Results

<img src="https://github.com/azyner/TinyMotorTests/blob/master/images/motorThrustTest.png" width="900">

| Motor                   | Batt   | Prop     | Velocity @ 3m altitude (meters / second) |
| ----------------------- | ------ | -------- | ---------------------------------------- |
| 0615 19k.kv mmw         | 205mah | 2-blade  | 5.81                                     |
| 0615 19k.kv mmw         | 255mah | 2-blade  | 6.00                                     |
| 0615 18k.kv boldclash   | 205mah | 2-blade  | 5.46                                     |
| 0617 25k.kv mmw         | 255mah | 2-blade  | 7.10                                     |
| 0716 17k.kv mmw         | 255mah | 2-blade  | 5.76                                     |

The 25000kv motors really stand out here. Significantly. The results here don't show much difference between 6mm 19k.kv and 7mm 17k.kv, which surprised me. That extra inertia really does pull down the acceleration. Outdoors though, 7mm really does shine as it handles the wind better with having a little extra momentum. The extra weight of the 255mah battery is visible in the 19000kv motors as the lighter 205mah battery starts faster, and the heavier battery with more current supply speeds past it later.

Extra graphs of all the runs can be seen in the experiments folder. You can also find a dump of my settings there. (betaflight 3.0.1)

## Future work
More tests! Other things to test:

* Flight controllers. Outside of these tests, I have noticed significant differences depending on the flight controller, both an Acrowhoop F3 and a beecore F3 do not seem to have the same top end thrust given the same motors as a Beebrain F1. A FC test would be very valuable, and it is sensitive to the tuning  as well.
* Propeller test. Do the 7mm motors perform better with 4 blades? Are the tri-blades a good balance between 2 and 4?
* HV vs 4.2. Not as valuable to me, but quantifying it is always good.

And of course, I'm open to suggestions!

I'll update this page when I run new experiments.

--Alex Zyner
