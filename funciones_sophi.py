from experta import *

class MedicalAgent(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(start="False")

    @Rule(Fact(start="False"),
          NOT(Fact(blurred_vision=W())),
          salience = 100)
    def Q1(self):

        """
        Sophia Albarrán 
        This function asks the user if they have blurred vision and stores the answer in a fact.
        """
        self.declare(Fact(blurred_vision=input("Do you have blurred vision?(yes/no) ")))
        
    @Rule(Fact(start="False"),
          NOT(Fact(floaters=W())),
          Fact(blurred_vision = 'yes'),
          salience = 99)
    def Q2(self):
        
        """
        Sophia Albarrán
        Based on the information asked before about the blurred vision, if the answer is yes, then. 
        This function asks the user if they see floaters and stores the answer in a fact.
        """
        self.declare(Fact(floaters=input("Do you see floaters? (yes/no) ")))
        
    @Rule(Fact(start="False"),
          NOT(Fact(loss_of_vision=W())),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'yes'),
          salience = 98)
    def Q3(self):
        
        """
        Sophia Albarrán
        Based on the information asked before about the floaters and the blurred vision, if the answer is yes on both of them, then.
        This function asks the user if they have experienced sudden loss of vision and stores the answer in a fact.
        """
        self.declare(Fact(loss_of_vision=input("Have you experienced sudden loss of vision? (yes/no) ")))

    @Rule(Fact(start='False'),
          Fact(loss_of_vision = 'yes'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'yes'),
          salience= 97)
    def print_retinal(self):
        
        """
        Sophia Albarrán
        Based on the information asked before about the floaters, blurred vision and loss of vision, if the answer is yes on all of them, then.
        This function informs the user that they may have a retinal detachment and advises them to seek medical attention.
        """
        
        print("You may have a retinal detachment. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start='False'),
          NOT(Fact(dark_spots=W())),
          Fact(loss_of_vision = 'no'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'yes'),
          salience = 96)
    def Q4(self):
        
        """
        Sophia Albarrán
        Based on the information asked before about the floaters and blurred vision, if the answer is yes on blurred vision, floaters and no on loss of vision then.
        This function asks the user if they have dark spots in their vision and stores the answer in a fact.
        """
        
        self.declare(Fact(dark_spots=input("Do you have dark spots in your vision? (yes/no)")))
        
        
    @Rule(Fact(start='False'),
          Fact(loss_of_vision = 'no'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'yes'),
          Fact(dark_spots = 'yes'),
          salience = 95)
    def print_retinopathy(self):
        
        """
        Sophia Albarrán         
        Based on the information asked before about the floaters, blurred vision and dark spots, if the answer is yes on all of them, then.
        This function informs the user that they may have diabetic retinopathy and advises them to seek medical attention.
        """
        
        print("You may have diabetic retinopathy. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start='False'),
          Fact(loss_of_vision = 'no'),
          Fact(blurred_vision = 'yes'),
          Fact(floaters = 'yes'),
          Fact(dark_spots = 'no'),
          salience = 94)
    def print_uveitis(self):
        
        """
        Sophia Albarrán
        Based on the information asked before about the floaters, blurred vision, dark spots, and loss of vision. if the answer is yes on blurred vision and floaters, no on dark spots and loss of vision then.
        This function informs the user that they may have uveitis and advises them to seek medical attention.
        """     
        
        print("You may have uveitis. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
engine = MedicalAgent()
engine.reset()  
engine.run() 