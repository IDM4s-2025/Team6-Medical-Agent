from experta import *

class MedicalAgent(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        yield Fact(start="False")

    @Rule(Fact(start="False"),
          NOT(Fact(blurred_vision=W())),
          salience=100)
    def Q1(self):
        """
        Elian Alejandro López de Alba
        This function asks the user if they have blurred vision and stores the answer in a fact.
        """
        self.declare(Fact(blurred_vision=input("Do you have blurred vision? (yes/no) ")))

    @Rule(Fact(start="False"),
          NOT(Fact(eye_redness=W())),
          salience=99)
    def Q7(self):
        """
        Elian Alejandro López de Alba
        This function asks the user if they have eye redness and stores the answer in a fact.
        """
        self.declare(Fact(eye_redness=input("Do you have eye redness? (yes/no) ")))

    @Rule(Fact(start="False"),
          NOT(Fact(double_vision=W())),
          salience=98)
    def Q12(self):
        """
        Elian Alejandro López de Alba
        This function asks the user if they experience double vision and stores the answer in a fact.
        """
        self.declare(Fact(double_vision=input("Do you experience double vision? (yes/no) ")))

    @Rule(Fact(start="False"),
          NOT(Fact(gritty_feeling=W())),
          salience=97)
    def Q13(self):
        """
        Elian Alejandro López de Alba
        This function asks the user if they have a gritty feeling in their eye and stores the answer in a fact.
        """
        self.declare(Fact(gritty_feeling=input("Do you have a gritty feeling in your eye? (yes/no) ")))

    @Rule(Fact(start='False'),
          Fact(double_vision='yes'),
          salience=96)
    def print_strabismus(self):
        """
        Elian Alejandro López de Alba
        If the user experiences double vision, this function suggests a possible case of Strabismus/Diplopia.
        """
        print("You may have Strabismus or Diplopia. Please consult an ophthalmologist.")
        self.modify(self.facts[1], start='True')

    @Rule(Fact(start='False'),
          Fact(eye_redness='yes'),
          Fact(gritty_feeling='yes'),
          salience=95)
    def print_blepharitis(self):
        """
        Elian Alejandro López de Alba
        If the user has both eye redness and a gritty feeling in the eye, this function suggests a possible case of Blepharitis.
        """
        print("You may have Blepharitis. Please seek medical attention.")
        self.modify(self.facts[1], start='True')

    
engine = MedicalAgent()
engine.reset()  
engine.run() 