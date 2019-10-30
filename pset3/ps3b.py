# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        #generating a random number
        number = random.random()
        
        if number <= self.getClearProb():
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        #generating a random number
        number = random.random()
        
        if number <= (self.getMaxBirthProb() * (1 - popDensity)):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxpop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses
        


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxpop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)        


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses = self.viruses.copy()
        
        for virus in viruses:
            if virus.doesClear():
                self.viruses.remove(virus)
                
        popdensity = len(self.viruses)/ self.maxpop
        
        viruses_after = self.viruses.copy()
        for virus in viruses_after:
            try:
                virus.reproduce(popdensity)
                self.viruses.append(virus)
            except NoChildException:
                continue
            
                
                
                    


#from ps3b_precompiled_36 import *
#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    numtimesteps = 300
    
    #list for viruses
    viruses = []
    # generating instances of simplevirus
    for i in range(numViruses):
        virus = SimpleVirus(maxBirthProb, clearProb)
        
        #adding that created virus in the list
        viruses.append(virus)
        
    #creating a patient class with the above created viruses list
    patient = Patient(viruses, maxPop)
    
    #to store data for each trial
    data = []
    
    for j in range(numTrials):
        timesteps = []
        # to store virus population after each time step
        virus_population = []
        
        for i in range(numtimesteps):
            timesteps.append(i)
            #print("Population before", patient.getTotalPop())
            patient.update()
            #print("Population after", patient.getTotalPop())
            
            #adding the virus population for that instance of time step
            virus_population.append(patient.getTotalPop())
        
        #adding data for each trial of all time steps
        data.append(virus_population)
    
    #print(data)
    
    #to store averages for each time step
    averages = []
    #to keep track of each timestep for each trial of data
    count = 0
    
    while True:
        total = 0
        for each_data in data:
            total += each_data[count]
        
        #calculating the average
        avg = total/len(data)
        averages.append(avg)
        
        count += 1
        
        if count == numtimesteps:
            break
    
    #print("Averages are", averages)
    #print(timesteps)
#==============================================================================
#     pylab.figure("Graph")
#     pylab.xlabel("Time Steps")
#     pylab.ylabel("Virus Population")
#     pylab.title("Population Variation")
#     pylab.plot(timesteps, averages, label = "population variation")
#     pylab.legend()
#==============================================================================
    
    pylab.plot(averages, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
        
    



#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        SimpleVirus.__init__(self,maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        try:
            return self.resistances[drug]
        except KeyError:
            return False


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        number = random.random()
        
        #checking if virus is resistant to all the drugs
        numdrugs = len(activeDrugs)
        #counter to note number of drugs the virus is resistant to
        count = 0
        
        for drug in activeDrugs:
            if self.isResistantTo(drug) == True:
                count += 1
        
        #check if count == number of drugs that is it is resistant to all drugs
        if count == numdrugs and (number <= self.maxBirthProb * (1 - popDensity)):
            # checking if the offspring would mutate that is change drug resistance
            #in self.resistances list
            
            #genearting another number to see if offspring wud inherit resistance
            number = random.random()
            
            #print("Number for mut is", number)
            
            if number <= (1 - self.mutProb):
                #reproduce as it is
                return ResistantVirus(self.maxBirthProb, self.clearProb, self.resistances,self.mutProb )
            else:
                #then apply resistance ie change values of keys in self.resistances from false to true and vice versa
                copy_resistances = self.resistances.copy()
                
                #test
                #number2 = random.random()
                
                for keys in self.resistances:
                    number2 = random.random()
                    if copy_resistances[keys] == True and number2 <= self.mutProb:
                        copy_resistances[keys] = False
                    else:
                        copy_resistances[keys] = True
                    
                
                #print(copy_resistances)
                
                return ResistantVirus(self.maxBirthProb, self.clearProb, copy_resistances ,self.mutProb )
                        
            
        else:
            raise NoChildException
            

        
        
            

                

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self.drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugs 


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        #getting the list of viruses the patient has
        viruses_inbody = self.getViruses()
        #viruses_inbody = self.viruses
        
        #TEST
        #print("Virus List is:", viruses_inbody)
        
        #the patient will contain instances of simplevirus and resistantvirus
        # so using attributeerror to differentiate bw them
        number_of_virus = 0
        
        for virus in viruses_inbody:
            try:
                count = 0
                #checking if this virus particle is resistant to all the drugs in the list
                for drug in drugResist:
                    if virus.isResistantTo(drug):
                        count += 1
                        #number_of_virus += 1
                
                if count == len(drugResist):
                    number_of_virus += 1
                    #print("number_of_virus", number_of_virus)
            except AttributeError:
                continue
        
        return number_of_virus
        

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        virus_list = self.viruses.copy()
        
        for virus in virus_list:
            if virus.doesClear():
                self.viruses.remove(virus)
        
        popdensity = len(self.viruses)/self.getMaxPop()
        
        viruslist = self.viruses.copy()
        for virus in viruslist:
            try:
                virus.reproduce(popdensity, self.drugs)
                self.viruses.append(virus)
            except NoChildException:
                continue
        


#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
#==============================================================================
#     #numsteps = 300
#     #creating a list of 100 resistant viruses
#     viruses = []
#     for i in range(numViruses):
#         virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb )
#         viruses.append(virus)
#         
#     #patient = TreatedPatient(viruses, maxPop)
#     
#     #to store data for each trial
#     data_for_virus = []
#     data_for_rvirus = []
#     
#     for j in range(numTrials):
#         
#         #creating a patient of 100 resistant viruses otherwise if instantiated
#         #outside loop than same decreased population wud be used for each trial
#         patient = TreatedPatient(viruses, maxPop)
#         
#         timesteps = []
#         virus_population = []
#         resistant_virus_population = []
#         #print("Virus population is", virus_population)
#         for i in range(150):
#             #timesteps.append(i)
#             patient.update()
#             virus_population.append(patient.getTotalPop())
#             #print(patient.getPrescriptions())
#             resistant_virus_population.append(patient.getResistPop(["guttagonol"]))
#         
#         #adding drug after 150 timesteps
#         patient.addPrescription("guttagonol")
#                        
#         for k in range(150):
#             #print(patient.getPrescriptions())
#             #timesteps.append(k)
#             patient.update()
#             virus_population.append(patient.getTotalPop())
#             #print("Resistant", patient.getResistPop(['guttagonol']))
#             resistant_virus_population.append(patient.getResistPop(["guttagonol"]))
#         #print("Timesteps:", timesteps)
#         print("virus population data for a single trial",virus_population )
#         #print("Resistant population:", resistant_virus_population)
#         #adding data as a list for each trial
#         #data.append(virus_population)
#         
#         #adding data into array for each trial
#         data_for_virus.append(virus_population)
#         data_for_rvirus.append(resistant_virus_population)
#     
#     #print(data_for_virus)
#     
#     #to calculate averages
#     for i in range(300):
#         timesteps.append(i)
#         
#         
#     averages = []
#     resistant_avg = []
#     #to keep track of each timestep for each trial of data
#     count = 0
#     
#     while True:
#         total = 0
#         for each_data in data_for_virus:
#             total += each_data[count]
#         
#         #calculating the average
#         avg = total/len(data_for_virus)
#         averages.append(avg)
#         
#         count += 1
#         
#         if count == 300:
#             break
#     
#     count = 0
#     
#     while True:
#         total = 0
#         for each_data in data_for_rvirus:
#             total += each_data[count]
#         
#         #calculating the average
#         avg = total/len(data_for_rvirus)
#         resistant_avg.append(avg)
#         
#         count += 1
#         
#         if count == 300:
#             break
#     
#     print(averages)
# 
#     #Plotting
#     pylab.figure()
#     pylab.xlabel("Time Steps")
#     pylab.ylabel("Virus Population")
#     pylab.title("Virus Population Variation with Drugs")
#     
#     pylab.plot(averages, label = "varrying Population")
#     pylab.plot(resistant_avg, label = "Resistant Population")
#     pylab.legend(loc = "best")
#     pylab.show()
#    
# 
#==============================================================================


    import numpy as np
    
    data = np.zeros(300)
    data1 = np.zeros(300)
    for i in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        virus_count, resist_virus_count = [], []
        for j in range(150):
            patient.update()
            virus_count.append(patient.getTotalPop())
            resist_virus_count.append(patient.getResistPop(['guttagonol']))
        patient.addPrescription('guttagonol')
        for k in range(150):
            patient.update()
            virus_count.append(patient.getTotalPop())
            resist_virus_count.append(patient.getResistPop(['guttagonol']))
        data = data + virus_count
        data1 = data1 + resist_virus_count
    data_avg = data/numTrials
    data1_avg = data1/numTrials
    
    pylab.plot(list([float('{0:.1f}'.format(i)) for i in data_avg]), label = r'Non-resistant population')
    pylab.plot(list([float('{0:.1f}'.format(j)) for j in data1_avg]), label = r'Guttagonol Resistant population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Average Virus Population')
    pylab.title(r'Virus Simulation in Patient')
    pylab.legend()
    pylab.show()