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
        Mauricio Loera 
        This function asks the user if they have blurred vision and stores the answer in a fact.
        """
        self.declare(Fact(blurred_vision=input("Do you have blurred vision? (yes/no) ")))

    @Rule(Fact(start="False"),
          NOT(Fact(eye_redness=W())),
          Fact(blurred_vision = 'no'),
          salience = 99)
    def Q7(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is no, 
        this function asks the user if they have eye redness and stores the answer in a fact.
        """
        self.declare(Fact(eye_redness=input("Do you have eye redness? (yes/no) ")))

    @Rule(Fact(start="False"),
          NOT(Fact(eye_pain=W())),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          salience = 98)
    def Q8(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no" and on Q7 is "yes",
        this function asks the user if they have experienced eye pain and stores the answer in a fact.
        """
        self.declare(Fact(eye_pain=input("Do you experience eye pain? (yes/no) ")))

    @Rule(Fact(start="False"),
          NOT(Fact(photophobia=W())),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'yes'),
          salience = 97)
    def Q9(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes" and on Q8 is "yes",
        this function asks the user if they are sensitive to light and stores the answer in a fact.
        """
        self.declare(Fact(photophobia=input("Are you sensitive to light (photophobia)? (yes/no) ")))

    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'yes'),
          Fact(photophobia = 'yes'),
          salience= 96)
    def print_uveitis(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "yes" and on Q9 is "yes",
        this function informs the user that they may have uveitis and advises them to seek medical attention.
        """
        
        print("You may have uveitis. Please seek medical attention.")
        self.modify(self.facts[1], start='True')

    @Rule(Fact(start="False"),
          NOT(Fact(nausea=W())),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'yes'),
          Fact(photophobia = 'no'),
          salience = 95)
    def Q10(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "yes" and on Q9 is "no",
        this function asks the user if they have experienced nausea of vomiting and stores the answer in a fact.
        """
        self.declare(Fact(nausea=input("Do you experience nausea or vomiting? (yes/no) ")))

    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'yes'),
          Fact(photophobia = 'no'),
          Fact(nausea = 'yes'),
          salience= 94)
    def print_glaucoma(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "yes", on Q9 is "no" and on Q10 is "yes",
        this function informs the user that they may have glaucoma and advises them to seek medical attention.
        """
        
        print("You may have glaucoma. Please seek medical attention.")
        self.modify(self.facts[1], start='True')

    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'yes'),
          Fact(photophobia = 'no'),
          Fact(nausea = 'no'),
          salience= 93)
    def print_stye(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "yes", on Q9 is "no" and on Q10 is "no",
        this function informs the user that they may have a stye and advises them to seek medical attention.
        """
        
        print("You may have a stye. Please seek medical attention.")
        self.modify(self.facts[1], start='True')

    @Rule(Fact(start="False"),
          NOT(Fact(discharge=W())),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'no'),
          salience = 92)
    def Q11(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes" and on Q8 is "no",
        this function asks the user if they have discharge from their eye and stores the answer in a fact.
        """
        self.declare(Fact(discharge=input("Do you have discharge from your eye? (yes/no) ")))

    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'no'),
          Fact(discharge = 'yes'),
          salience= 91)
    def print_conjuntivitis(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "no" and on Q11 is "yes",
        this function informs the user that they may have conjuntivitis and advises them to seek medical attention.
        """
        
        print("You may have conjuntivitis. Please seek medical attention.")
        self.modify(self.facts[1], start='True')

    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'yes'),
          Fact(eye_pain = 'no'),
          Fact(discharge = 'no'),
          salience= 90)
    def print_blepharitis(self):
        
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "no" and on Q11 is "no",
        this function informs the user that they may have blepharitis and advises them to seek medical attention.
        """
        
        print("You may have blepharitis. Please seek medical attention.")
        self.modify(self.facts[1], start='True')

engine = MedicalAgent()
engine.reset()
engine.run()