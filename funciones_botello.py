from experta import *

class MedicalAgent(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(start="False")
        
    @Rule(Fact(start="False"),
          NOT(Fact(greetings=W())),
          salience= 100)
    def greet(self):
        """
        Eduardo Botello Casey
        This function greets the user and asks for their name.
        """
        self.declare(Fact(greetings=input("Hello! I am a medical agent made for Ophthalmology. What is your name? ")))
          

    @Rule(Fact(start="False"),
          Fact(greetings=W()),
          NOT(Fact(blurred_vision=W())),
          salience = 99)
    def Q1(self):
        """
        Eduardo Botello Casey
        This function asks the user if they have blurred vision and stores the answer in a fact.
        """
        self.declare(Fact(blurred_vision=input("Do you have blurred vision? (yes/no) ")))
        
    @Rule(Fact(start="False"),
          NOT(Fact(floaters=W())),
          Fact(blurred_vision = 'yes'),
          salience = 98)
    def Q2(self):
        """
        Eduardo Botello Casey
        If the user answers 'yes' to blurred vision, this function asks if they have floaters and stores the answer in a fact.
        """
        self.declare(Fact(floaters=input("Do you see floaters? (yes/no) ")))
        
    @Rule(Fact(start="False"),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'no'),
          salience = 93)
    def Q5(self):
        """
        Eduardo Botello Casey
        If the user answers 'yes' to blurred vision and 'no' to floaters, 
        this function asks if they see straight lines as wavy and stores the answer in a fact.
        """
        self.declare(Fact(lines=input("Do straight lines appear wavy to you? (yes/no) ")))

    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'no'),
          Fact(lines = 'yes'),
          salience= 92)
    def print_AMB(self):
        """
        Eduardo Botello Casey
        If the user answers 'yes' to blurred vision, 'no' to floaters, and 'yes' to lines appearing wavy,
        this function indicates that the user may have Age-related Macular Degeneration (AMD).
        """
        print("You may have Age-related Macular Degeneration (AMD). Please seek medical attention. ")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'no'),
          Fact(lines = 'no'),
          salience = 91)
    def Q6(self):
        """
        Eduardo Botello Casey
        If the user answers 'yes' to blurred vision and 'no' to floaters and 'no' to lines appearing wavy,
        this function asks if they see halos around lights and stores the answer in a fact.
        """
        self.declare(Fact(halos=input("Do you see halos around lights? (yes/no) ")))
        
    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'no'),
          Fact(lines = 'no'),
          Fact(halos = 'yes'),
          salience = 90)
    def print_Glaucoma(self):
        """
        Eduardo Botello Casey
        If the user answers 'yes' to blurred vision, 'no' to floaters, 'no' to lines appearing wavy, and 'yes' to halos around lights,
        this function indicates that the user may have Glaucoma.
        """
        print("You may have Glaucoma. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'no'),
          Fact(lines = 'no'),
          Fact(halos = 'no'),
          salience = 89)
    def print_Cataracts(self):
        """
        Eduardo Botello Casey
        If the user answers 'yes' to blurred vision, 'no' to floaters, 'no' to lines appearing wavy, and 'no' to halos around lights,
        this function indicates that the user may have Cataracts.
        """
        print("You may have Cataracts. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
engine = MedicalAgent()
engine.reset()
engine.run()
