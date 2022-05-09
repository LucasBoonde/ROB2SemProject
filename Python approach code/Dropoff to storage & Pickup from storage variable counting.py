from robodk.robolink import *                       # import the robolink library (bridge with RoboDK)
from robodk.robomath import *
RDK = Robolink()                                    # establish a link with the simulator
robot = RDK.Item('UR5')                             # retrieve the robot
SafePos = RDK.Item('SafePos')                       #main Safe position
SafePosPick = RDK.Item('SafePosPick')               #defines safe position for pickup
HandoverZone1 = RDK.Item('HandoverZone1')           #defines handover zone1 dropoff
SafePosDrop = RDK.Item('SafePosDrop')               #defines safe position for dropoff
HandoverZone2 = RDK.Item('HandoverZone2')           #defines handover zone 2 dropoff
def close_gripper():                                #defines 'Close_gripper' as the function
    robot.setDO(0,0)
    robot.setDO(1,1)
def open_gripper():                                 #defines 'open_gripper' as the function
    robot.setDO(0,1)
    robot.setDO(1,1)                                               
App_HZ1 = HandoverZone1.Pose()*transl(0,0,-50)      #defines the approach as 50mm above the handover zone 1 position
App_HZ2 = HandoverZone2.Pose()*transl(0,0,-50)      #defines the approach as 50mm above the handover zone 2 position
robot.MoveJ(SafePos)                                #moves to safety position before start
open_gripper()                                      #open gripper
between_dist = 63.5                                 #one block space between
x_axis = 0                                          # x-axis variable. for keeping track of how many blocks have been dropped off. Should reset once y variable goes up by one. 
x_axis_limit = 5                                    # x-axis limit. limits how many blocks can be placed in a row. 
y_axis = 0                                          # y-axis variable. for keeping track of what row the robot should fill out. should go up by one once the x-axis limit is reached
y_axis_limit = 1                                    # y-axis limit. Limits how many rows the robot can make.

#dropoff function
def dropoff_function():
    robot.MoveJ(App_HZ2)                                                                    #moves to approach for handover zone 2
    robot.MoveL(HandoverZone2)                                                              #moves to handover zone 2
    close_gripper()                                                                         #Close gripper
    robot.MoveL(App_HZ2)                                                                    #moves to approach for handover zone 2
    robot.MoveJ(SafePos)
    robot.MoveJ(SafePosDrop)                                                                #moves to safe position for dropoff function
    target = RDK.Item('DropOff')                                                            #define target from where the rest of the array is made
    approach = target.Pose()*transl(between_dist*x_axis,-between_dist*y_axis,-50)           #defines the approach to the target as 50mm up the z-axis. also translates the coordinates along the x-axis for each iteration also moves it down the y-axes the between distance.
    robot.MoveJ(approach)                                                                   #moves to approach position
    target = target.Pose()*transl(between_dist*x_axis,-between_dist*y_axis,0)               #redefines the target the between distance along x-axis for each iteration also moves it down the y-axes the between distance.
    robot.MoveL(target)                                                                     #moves to the target
    open_gripper()                                                                          #open gripper
    robot.MoveL(approach)                                                                   #moves to apporach
    robot.MoveJ(SafePosDrop)                                                                #moves to safe position for dropoff function
    robot.MoveJ(SafePos)                                                                    #moves to safe position
    if x_axis < x_axis_limit:                                                               #if statement checking if the x-axis exceeds the limit if it doesn't it adds +1
        x_axis+=1
    elif y_axis < y_axis_limit:                                                             #else if doing the same for y-axis and resets the x-axis
        y_axis+=1
        x_axis = 0

#pickup function
def pickup_function():
    robot.MoveJ(SafePos)                                                                    #moves to safety position
    target = RDK.Item('Pickup')                                                             #define target from where the rest of the array is made
    approach = target.Pose()*transl(between_dist*i,1*i,-50)*transl(0,between_dist,0)        #defines the approach to the target as 50mm up the z-axis. also translates the coordinates along the x-axis for each iteration also moves it down the y-axes the between distance.
    robot.MoveJ(approach)                                                                   #moves to approach position
    target = target.Pose()*transl(between_dist*i,1*i,0)*transl(0,between_dist,0)            #redefines the target the between distance along x-axis for each iteration also moves it down the y-axes the between distance.
    robot.MoveL(target)                                                                     #moves to the target
    close_gripper()                                                                         #close gripper
    robot.MoveL(approach)                                                                   #moves to apporach
    robot.MoveJ(SafePosPick)                                                                #moves to safe position for pickup function
    robot.MoveJ(App_HZ1)                                                                    #moves to approach for handover zone 1
    robot.MoveL(HandoverZone1)                                                              #moves to handover zone 1
    open_gripper()                                                                          #open gripper
    robot.MoveL(App_HZ1)                                                                    #moves to approach for handover zone 1
    robot.MoveJ(SafePosPick)                                                                #moves to safe position for pickup function
    robot.MoveJ(SafePos)                                                                    #moves to safety position    
# main code (loop code)
dropoff_function()
    #function that creates button on the teaching pendant asking if we want to run funtion dropoff or function pickup and sends a corresponding signal to the below if else statement.
    #if else statement that runs either function dropoff or funtion pickup depending on input from the button push.


