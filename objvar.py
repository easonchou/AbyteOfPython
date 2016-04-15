class Robot:
    '''Represents a robot, with a name.'''
    
    #A class variable, counting the number of robots
    
    population = 0
    
    def __init__(self, name):
        '''Initialize the data.'''
        self.name = name
        print('(Initialize {0})'.format(self.name))
        
        #when this person is created, the robot 
        # adds to population
        
        Robot.population += 1
        
    def __del__(self):
        '''I am dying'''
        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))
    
    def sayHi(self):
        '''Greating by robot.
        Yeah, they can do that.'''
        print('Greetings, my master call me {0}.'.format(self.name))
        
    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
        
    @staticmethod
    def howMany2():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))   
        
    howMany = staticmethod(howMany) 
    
driod1 = Robot('R2-D2')
driod1.sayHi()
#driod1.howMany()
Robot.howMany()

driod2 = Robot('C-3P0')
driod2.sayHi()
Robot.howMany()

print('\nRobots can do some work here.\n')

print("Robots have finished their work. So let's destroy them.")

del driod1
del driod2

Robot.howMany()


