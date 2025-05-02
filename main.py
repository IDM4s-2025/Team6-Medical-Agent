from experta import *

class MedicalAgent(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(start="False")

    @Rule(Fact(start="False"),
          NOT(Fact(greetings=W())),
          salience= 150)
    def greet(self):
        """
        Eduardo Botello Casey
        This function greets the user and asks for their name.
        """
        self.declare(Fact(greetings=input("Hello! I am a medical agent made for Ophthalmology. What is your name? ")))

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
        
        self.declare(Fact(dark_spots=input("Do you have dark spots in your vision? (yes/no) ")))
        
        
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
    
    @Rule(Fact(start="False"),
          NOT(Fact(eye_redness=W())),
          Fact(blurred_vision = 'no'),
          salience = 88)
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
          salience = 87)
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
          salience = 86)
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
          salience= 85)
    def print_uveitis2(self):
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
          salience = 84)
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
          salience= 83)
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
          salience= 82)
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
          salience = 81)
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
          salience= 80)
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
          salience= 79)
    def print_blepharitis(self):
        """
        Mauricio Loera
        If the answer on Q1 is "no", on Q7 is "yes", on Q8 is "no" and on Q11 is "no",
        this function informs the user that they may have blepharitis and advises them to seek medical attention.
        """
        print("You may have blepharitis. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start="False"),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'no'),
          NOT(Fact(double_vision=W())),
          salience=78)
    def Q12(self):
        """
        Elian Alejandro López de Alba
        This function asks the user if they experience double vision and stores the answer in a fact.
        """
        self.declare(Fact(double_vision=input("Do you experience double vision? (yes/no) ")))
    
    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'no'),
          Fact(double_vision='yes'),
          salience=77)
    def print_strabismus(self):
        """
        Elian Alejandro López de Alba
        If the user experiences double vision, this function suggests a possible case of Strabismus/Diplopia.
        """
        print("You may have Strabismus or Diplopia. Please consult an ophthalmologist.")
        self.modify(self.facts[1], start='True')

    @Rule(Fact(start="False"),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'no'),
          Fact(double_vision='no'),
          NOT(Fact(gritty_feeling=W())),
          salience=76)
    def Q13(self):
        """
        Elian Alejandro López de Alba
        This function asks the user if they have a gritty feeling in their eye and stores the answer in a fact.
        """
        self.declare(Fact(gritty_feeling=input("Do you have a gritty feeling in your eye? (yes/no) ")))
    
    
    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'no'),
          Fact(double_vision='no'),
          Fact(gritty_feeling='yes'),
          salience=75)
    def print_dry_eye(self):
        """
        Elian Alejandro López de Alba
        If the user hasn't both eye redness and a gritty feeling in the eye, this function suggests a possible case of Dry Eye Syndrome.
        """
        print("You may have Dry Eye Syndrome. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start='False'),
          Fact(blurred_vision = 'no'),
          Fact(eye_redness = 'no'),
          Fact(double_vision='no'),
          Fact(gritty_feeling='no'),
          salience=74)
    def print_amblyopia(self):
        """
        Elian Alejandro López de Alba
        If the user hasn't both eye redness and a doesn't have a gritty feeling in the eye, this function suggests a possible case of Amblyopia.
        """
        print("You may have Amblyopia. Please seek medical attention.")
        self.modify(self.facts[1], start='True')
    
    @Rule(Fact(start='True'),
          Fact(greetings=MATCH.greetings))
    def print_goodbye(self, greetings):
        """
        Eduardo Botello Casey
        This function informs the user that the conversation is over and thanks them for their time.
        """
        print("Thank you for your time", greetings + ". Goodbye!")
        
    
engine = MedicalAgent()
engine.reset()  
engine.run() 