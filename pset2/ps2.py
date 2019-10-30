# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleanedtiles = []
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #converting the tuple of floats into ints
        x, y = int(pos.getX()), int(pos.getY())
        if (x, y) not in self.cleanedtiles:
            self.cleanedtiles.append((x, y))

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m , n) in self.cleanedtiles
            
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleanedtiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randint(0, self.width - 1 )
        y = random.randint(0, self.height - 1)
        
        return (Position(x, y))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
#        x = int(pos.getX())
#        y = int(pos.getY())
        
        if (pos.getX() < 0 or pos.getY() < 0):
            return False
        elif (pos.getX() >= self.width or pos.getY() >= self.height):
            return False
       
        else:
            return True
            


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randrange(0, 360)
        self.position = self.room.getRandomPosition()
        
        #THE GRADER WAS FAILING THE TEST TO CHECK IF THE TILE AT 
        #WHICH ROBOT IS CREATED IS CLEAN OR NOT IN updatePositionAndClean
        # SO THE SOLUTION WAS to add that tile as clean here when
        # robot is generated 
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #self.room.cleanTileAtPosition(self.getRobotPosition())
        #this is a position object position(x, y)
        currentposition = self.getRobotPosition()
        #self.room.cleanTileAtPosition(currentposition)
        
        #print("At start clean tiles:", self.room.getNumCleanedTiles())
        
        #add the position where it started from to be clean
        
        #print("position before:", currentposition)
        
        while (True):
            #get the new posiition through the position class
            newposition = currentposition.getNewPosition(self.direction, self.speed)
            #print("New position:", newposition)
            #check if the newposition is in the room
            if (self.room.isPositionInRoom(newposition)):
                break
            else:
                #change the direction at random
                self.setRobotDirection(random.randrange(0, 360)) 
        
        
        #set the newposition as the position of robot
        self.setRobotPosition(newposition)
        #adding the new tile as to be cleaned
        self.room.cleanTileAtPosition(newposition)
        
        
        #print("At end clean tiles:", self.room.getNumCleanedTiles())

#Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    #to store clockticks for each trial
    clock_ticks_per_trial = []
    
    for i in range(num_trials):
        
        #creating room
        room = RectangularRoom(width, height)
    
        #creating robots of type robot_type and storing them in a list
        robots = []
        for i in range(num_robots):
            robot = robot_type(room, speed)
            robots.append(robot)
    
    
        #calculating the fraction of cleaned tiles
        min_coverage_pertrial = round(min_coverage, 2)
        fraction_trial = round(room.getNumCleanedTiles() / room.getNumTiles(), 2)
        
        #the clock tick counter
        clock = 0
        
        #stops when all tiles have been cleaned
        while fraction_trial <= min_coverage_pertrial:
            #instantiate its cleaning method for each robot
            for robot in robots:
                robot.updatePositionAndClean()
            
            #incrementing the clock tick
            clock += 1
            
            #updating the number of cleaned tiles
            count = room.getNumCleanedTiles()
            
            #updating fraction
            fraction_trial = round(room.getNumCleanedTiles() / room.getNumTiles(), 2)
            
            #print("At end of iteration clock tick:", clock, "cleaned:", count)
            
    
        #print("Took", clock, "clock ticks to clean")
        
        #adding the clock tick for this trial in array
        clock_ticks_per_trial.append(clock)
        
    #print(clock_ticks_per_trial)
    mean = sum(clock_ticks_per_trial)/len(clock_ticks_per_trial)
    return mean

# Uncomment this line to see how much your simulation takes on average
##print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #get the current position of this robot
        currentposition = self.getRobotPosition()
        
        #changing the intial direction
        self.setRobotDirection(random.randrange(0, 360))
        
        while(True):
            #Test
#            while(True):
#                #get a random direction
#                direction = random.randrange(0, 360)
#                if(direction == self.direction):
#                    continue
#                else:
#                    break
            #end test 
            #get a random direction
            direction = random.randrange(0, 360)
            newposition = currentposition.getNewPosition(direction, self.speed)
            
            if (self.room.isPositionInRoom(newposition)):
                break
            else:
                #change the direction at random
                self.setRobotDirection(random.randrange(0, 360)) 
        
        
        #set the newposition as the position of robot
        self.setRobotPosition(newposition)
        #adding the new tile as to be cleaned
        self.room.cleanTileAtPosition(newposition)


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#