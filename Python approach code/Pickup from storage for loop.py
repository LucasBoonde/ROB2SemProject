from robodk.robolink import *                                   # import the robolink library (bridge with RoboDK)
from robodk.robomath import *
RDK = Robolink()                                                # establish a link with the simulator
robot = RDK.Item('UR5')                                       # retrieve the robot
SafePos = RDK.Item('SafePos')                                   #main Safe position
SafePosPick = RDK.Item('SafePosPick')                           #defines safe position for pickup
HandoverZone1 = RDK.Item('HandoverZone1')                       #defines handover zone1 dropoff
def close_gripper():                                            #defines 'Close_gripper' as the function
    robot.setDO(0,0)
    robot.setDO(1,1)
def open_gripper():                                             #defines 'open_gripper' as the function
    robot.setDO(0,1)
    robot.setDO(1,1)                                               
App_HZ1 = HandoverZone1.Pose()*transl(0,0,-50)                  #defines the approach as 50mm above the handoverzone1 position
robot.MoveJ(SafePos)                                            #moves to safety position before start
open_gripper()                                                  #open gripper
between_dist = 63.5                                             #one block space between

for i in range(0,6):                                            #for loop to make 6 iteration for i 0-5
    robot.MoveJ(SafePos)                                        #moves to safety position
    target = RDK.Item('Pickup')                                 #define target from where the rest of the array is made
    approach = target.Pose()*transl(between_dist*i,1*i,-50)     #defines the approach to the target as 50mm up the z-axis. also translates the coordinates along the x-axis for each iteration
    robot.MoveJ(approach)                                       #moves to approach position
    target = target.Pose()*transl(between_dist*i,1*i,0)         #redefines the target the between distance along x-axis for each iteration
    robot.MoveL(target)                                         #moves to the target
    close_gripper()                                         #close gripper
    robot.MoveL(approach)                                       #moves to apporach
    robot.MoveJ(SafePosPick)                                    #moves to safe position for pickup function
    robot.MoveJ(App_HZ1)                                        #moves to approach for handover zone 1
    robot.MoveL(HandoverZone1)                                  #moves to handover zone 1
    open_gripper()                                           #open gripper
    robot.MoveL(App_HZ1)                                        #moves to approach for handover zone 1
    robot.MoveJ(SafePosPick)                                    #moves to safe position for pickup function
    robot.MoveJ(SafePos)                                                                    #moves to safety position
    
for i in range(0,6):                                                                        #for loop to make 6 iteration for i 0-5
    robot.MoveJ(SafePos)                                                                    #moves to safety position
    target = RDK.Item('Pickup')                                                             #define target from where the rest of the array is made
    approach = target.Pose()*transl(between_dist*i,1*i,-50)*transl(0,between_dist,0)        #defines the approach to the target as 50mm up the z-axis. also translates the coordinates along the x-axis for each iteration also moves it down the y-axes the between distance.
    robot.MoveJ(approach)                                                                   #moves to approach position
    target = target.Pose()*transl(between_dist*i,1*i,0)*transl(0,between_dist,0)            #redefines the target the between distance along x-axis for each iteration also moves it down the y-axes the between distance.
    robot.MoveL(target)                                                                     #moves to the target
    close_gripper()                                                                      #close gripper
    robot.MoveL(approach)                                                                   #moves to apporach
    robot.MoveJ(SafePosPick)                                                                #moves to safe position for pickup function
    robot.MoveJ(App_HZ1)                                                                    #moves to approach for handover zone 1
    robot.MoveL(HandoverZone1)                                                              #moves to handover zone 1
    open_gripper()                                                                      #open gripper
    robot.MoveL(App_HZ1)                                                                    #moves to approach for handover zone 1
    robot.MoveJ(SafePosPick)                                                                #moves to safe position for pickup function
    robot.MoveJ(SafePos)                                                                    #moves to safety position    