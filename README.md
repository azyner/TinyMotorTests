# TinyMotorTests
Analysis of single point tracking micro quadcopter punchout tests

# Abstract
This work uses a Motion Capture system to analyse the thrust performace of micro quad motors in situ. Each quad was set up with throttle on a switch to test the instantaneous acceleration of each motor set.

# Introduction
There are many different choices when picking micro quad motors. 7mm or 6mm? What about those new 6x17mm motors? I set out to which motors actually provide the best thrust in situ, that is to say I didn't want to do a static thrust test on a workbench. There are several reasons for this, but mainly its because given such small quads, there are a lot of unknown variables at play, inertia, air drag, losses due to battery droop, etc. All of these significantly change the flight style.

# Method
The recording system used is an OptiTrack http://optitrack.com/ system, which I was kindly given access to by the Aeronautical Deptartment at The University of Sydney. This system is accurate to 1mm at a rate of 120Hz, so its the best known testing environment for this experiment. To track the quadcopter, a single tracking 'dot' was placed on the quad, and the camera was removed to maintain weight. The dot is 3.8 grams, and the camera 4.0 grams, so the difference is minimal.

###PICTURE HERE of quad with dot###

Each set of motors was given at least three punchouts, and at least two different batteries. The batteries used are mylipo.de HV PH2.0 packs, charged to only 4.2V (NOT HV charge). I tested four sets of motors: boldclash 0615 18kkv, micro-motor-warehouse: 0615 19kkv, 0617 25kkv, and 0716 17kkv. The 0716 and boldclash motors were fresh, the other two had about an hour of flight time. The FC used is a BeeBrain FC 1.2, with P2.0 plug. The same FC was used for all the motors. Frames used are 0617 Cockroach, 0716 Beta65, and 0615 Eachine E010S (The white one). Props used are the standard whoop props, cut to 2 blade for all tests.

For each test, the quad was placed on the ground, and a switch throttle was used. I have data for the entire climb, and I compare velocities at 3m of altitude. After this I had to kill throttle to avoid hitting the ceiling. 

# Results

## CHARTS HERE ##

Talk about results.

# Future work
I plan on taking these measurements again for reproduction's sake, I learnt a lot in the first tests. Outside of these tests, I have also noticed significant differences depending on the flight controller, both an Acrowhoop F3 and a beecore F3 do not seem to have the same top end thrust given the same motors as a Beebrain F1, so I'd like to do a FC comparison as well.
