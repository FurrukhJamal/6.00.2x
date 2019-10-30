###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
   

    #get a copy of the dictionary
    cows_copy = cows.copy()
    #converting the dictionary into a sorted list of tuples
    tuplelist = []
    for keys in cows:
        tuplelist.append((cows[keys], keys))
        
    tuplelist.sort(reverse = True)
    #this will contain lists of trips with names of cows
    returnlist = []

    #list to track names of cows that has been taken
    takenitems = []

    #while there are cows to take away
    while (len(takenitems) != len(tuplelist) ):
        #list for each iteration/trip
        triplist = []
           
        #variable for limit so to maintain the intial limit for each trip
        templimit = limit
       
        for i in range(0, len(tuplelist)):
           
            # since list is sorted either the first wud be taken or the next
            if (int(tuplelist[i][0]) <= templimit):
                #checking if its already taken
                if tuplelist[i][1] in takenitems:
                    continue
                else:
                    #add the cow
                    triplist.append(tuplelist[i][1])
                    #update the remaining weight for the trip
                    templimit -= int(tuplelist[i][0])
                    
                    #adding the name remember what cows already taken
                    takenitems.append(tuplelist[i][1])
            else:
                continue
            
        
        # adding this trip list to the list that would be returned
        returnlist.append(triplist)
        
    
    return returnlist
        
            
            
                
                
            
            


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # to save all valid trips
    #validtrips = []
    
    #sorting the dictinoary as a tuple
    tuplelist = []
    
    for keys in cows:
        tuplelist.append((cows[keys], keys))
        
    tuplelist.sort(reverse = True)
    #print(tuplelist)
    trip = []
    
    for combinations in get_partitions(tuplelist):
        #trip = []
        #print(combinations, "\n\n")
        
        # a flag to determine if all combinations of trips are a valid
        # trip for this particular set
        counterflag = 0
        
        for possible_trip in combinations:
            templimit = limit
            
            #to iterate over all cows in one combination of trip
            for i in range(0, len(possible_trip)):
                #print("Name:", possible_trip[i][1], "Weight:", possible_trip[i][0])
                templimit -= int(possible_trip[i][0])
            
            #to check if this combination didnot exceed the limit
            if (templimit >= 0):
                #it was a valid combinatio hence add a counter
                # so that the counter could be checked in outer loop
                # if all trips of this particular combination is valid
                counterflag += 1
        
        if (counterflag == len(combinations)):
            #this means all the trips in this particular combination
            #did not exceed the weight limit hence it is a valid combination
            trip.append(combinations)
    
    #print(trip)
    
    #to record the least number of trips the valid combinations have
    min_number_trips = 0
    for i in range(0, len(trip) ):
        #print(len(trip[i]), "trip:", trip[i])
        
        #print("min variable is:", min_number_trips)
        if (min_number_trips == 0):
            min_number_trips = len(trip[i])
#        elif (len(trip[i + 1]) < min_number_trips):
#            min_number_trips = len(trip[i + 1])
            #print("Length ahead is:",len(trip[i + 1]) )
        else:
            #using a try block to avoid indexerror for list when
            # it reaches the last element and trip[i + 1] wud raise an error
            try:
                if(len(trip[i + 1]) < min_number_trips):
                    min_number_trips = len(trip[i + 1])
            except IndexError:
                continue
    
            
    #print("Min trips:", min_number_trips)       
    
    
    #eventual list that would contain a lists of trips w names
    #that consisted the leats amount of trips required to tranpsport
    #all the cows(determined by variable min_number_trips)
    returnlist = []
    for each in trip:
        arrayfortrips = []
        #print(each)
        
#        #going through each trip of valid trips
#        for i in range(0, len(each)):
#            #arrayfornames.append(each[i][1])
#            print("Each trip:",each[i])    
#        #retrunlist.append(arrayfornames)
        if (len(each) == min_number_trips):
            
            for items in each:
                #print("each trip:",items)
                names = []
                for everytuple in items:
                    #print(everytuple[1])
                    names.append(everytuple[1])
                    
                arrayfortrips.append(names)
        
            #print("Each Trip is:",arrayfortrips)
            returnlist.append(arrayfortrips)

    
    
    #now selecting a random combination from the list of trips
    import random
    index = random.randrange(len(returnlist))
                
    return returnlist[index]
            
            
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    starttimegreedy = time.time()
    greedy_cow_transport(cows)
    endtimegreedy = time.time()
    
    print("Time taken by Greedy:", endtimegreedy - starttimegreedy)
    
    starttimebrute = time.time()
    brute_force_cow_transport(cows)
    endtimebrute = time.time()
    
    print("Time taken by Brute Force:", endtimebrute - starttimebrute)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


