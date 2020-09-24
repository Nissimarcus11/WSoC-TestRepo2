class Sport:
    def __init__(self):
        self.name_of_sport=""
        self.type_of_sport=""
        self.no_of_players=""
        self.time_duration=""
        self.equipment=""
        self.country_of_origin=""
    def get_details(self):
        #method to print legend details
        str="""
        Name of the sport is {0}
        Type of sport is {1}
        Number of players required are {2}
        Time duration is {3}
        Equipment needed is {4}
        Country of origin is {5}        
        """
        print(str.format(self.name_of_sport,self.type_of_sport,self.no_of_players,self.time_duration,self.equipment,self.country_of_origin))
class Legend():
    def __init__(self):
        self.name=""
        self.country=""
        self.playing=""
        self.achievements=""

    def legend_details(self):
        str="""
        Name: {0}
        Country belogs: {1}
        Status: currently {2}
        Achievements:
        {3}
        """
        print(str.format(self.name,self.country,self.playing,self.achievements))


class Cricket(Sport):
    def __init__(self):
        self.name_of_sport="Cricket"
        self.type_of_sport="Outdoor"
        self.no_of_players="Eleven players in each team"
        self.equipment="Bat, Ball, Safety kit"
        self.country_of_origin="England"

        global cricket_legend1,cricket_legend2 #used global to access the variables in another method
        cricket_legend1=Legend() #object of legend class
        cricket_legend1.name="Sachin Ramesh Tendulkar"
        cricket_legend1.country="India"
        cricket_legend1.playing="not playing"
        cricket_legend1.achievements="""- He was the sport's first batsman to score a double century
        - The only player to have scored 100 centuries in internationals. 
        """

        cricket_legend2 = Legend()
        cricket_legend2.name="Brian Lara"
        cricket_legend2.playing="not playing"
        cricket_legend2.country="West Indies"
        cricket_legend2.achievements="""-The first man to score seven centuries in eight first-class innings
        -He was the fastest batsman to score 10,000 (with Sachin Tendulkar) 
         and 11,000 Test runs, in terms of number of innings.
        """


        
        
    def get_details(self,type):
        if(type==1):
            self.time_duration="around Three hours" #giving value
            super().get_details() #calling the method in super class- Sport class
        elif(type == 2):
            self.time_duration="around Eight hours "
            super().get_details()
        elif(type == 3):
            self.time_duration="around Three to Five days"
            super().get_details()
        elif(type==4):
            self.time_duration="ranging from three hours to five days"
            super().get_details()
        elif(type==5):
            cricket_legend1.legend_details() #calling method of legend class
            cricket_legend2.legend_details()
        # else:
        #     exit()

class Football(Sport):
    def __init__(self):
        self.name_of_sport="Football"
        self.type_of_sport="Outdoor"
        self.no_of_players="Eleven players in each team"
        self.time_duration="around 90 minutes"
        self.equipment="Football, goal posts, safety kit"
        self.country_of_origin="England"
        global football_legend1,football_legend2
        football_legend1 = Legend()
        football_legend1.name="Cristiano Ronaldo"
        football_legend1.country="Portugal"
        football_legend1.playing="playing"
        football_legend1.achievements="""-2017 FIFA Ballon d'Or
        -UEFA Best Player
        -2017 The Best FIFA Men’s Player
        """
        football_legend2=Legend()
        football_legend2.name="Lionel Messi"
        football_legend2.country="Argentina"
        football_legend2.playing="playing"
        football_legend2.achievements="""-The record for the most goals scored in La Liga in a season: 50 goals
        -The record for the most La Liga hat-tricks in a season: 8 hat-tricks
        """
    def get_details(self,type):
        if(type==1):
            super().get_details()
        elif(type==2):
            football_legend1.legend_details()
            football_legend2.legend_details()


class Badminton(Sport):
    def __init__(self):
        self.name_of_sport="Badminton"
        self.type_of_sport="can be played both indoor and outdoor"
        self.equipment="badminton racket, shuttle, net, and other accesories"
        self.time_duration="about an hour"
        self.country_of_origin="India"
        global badminton_legend1, badminton_legend2
        badminton_legend1 = Legend()
        badminton_legend2 = Legend()
        badminton_legend1.name="Lee Yong Dae"
        badminton_legend1.country="Korea"
        badminton_legend1.playing="Not playing"
        badminton_legend1.achievements="""-Asian Junior Championships – seven gold medals
        -World Junior Championships – three gold medals
        -Summer Universiade – three gold medals
        """
        badminton_legend2.name="Viktor Axelsen"
        badminton_legend2.country="Denmark"
        badminton_legend2.playing="playing"
        badminton_legend2.achievements="""-2016 Olympic Games bronze medal winner
        -BWF World Championships – gold medal in 2017, bronze medal in 2014
        -European Championships – first place in 2016 and 2018
        """
    
    def get_details(self,type):
        if(type==1):
            self.no_of_players="One player in each team"
            super().get_details()
        elif(type==2):
            self.no_of_players="Two players in each team"
            super().get_details()
        elif(type==3):
            self.no_of_players="one to two players in each team"
            super().get_details()
        elif(type==4):
            badminton_legend1.legend_details()
            badminton_legend2.legend_details()


    

def MainMenu():
    print("""
    Choose the option and enter the respective number
        1 -> Cricket
        2 -> Football
        3 -> Badminton
        9 -> Exit
    """)
    while(True):
        try:
            inpt=int(input("Enter the option: "))
            if(inpt==9):
                exit()
            if(inpt in range(1,5)):
                # condition to prevent false inputs
                break
            else:
                print("Please enter valid option: ")
        except Exception:
            #exception for duplicate values like strings
            print("Please enter valid option: ")
    if inpt==1:
        cricket_menu()
    elif inpt==2:
        football_menu()
    elif inpt==3:
        badminton_menu()

def cricket_menu():
    print("""
        Select a particular type:
            1 -> T20
            2 -> ODI
            3 -> Test
            4 -> Default
            5 -> Legends details
            8 -> Back
            9 -> Exit 
        """)
    
    while(True):
        try:
            inpt=int(input("Enter an option: "))
            if(inpt==9):
                exit()
            elif(inpt==8):
                MainMenu()
                break
            elif(inpt in range(1,6)):
                # print("passed")
                break
            else:
                print("Please enter valid option: ")
        except Exception:
            print("Please enter valid option: ") 
       
    cricket_obj.get_details(inpt)
    print("""   
        Press * to go back
        Press 0 to go to main menu 
        Press # to exit
    """)
    while(True):
        inpt = input("Enter Option: ")
        if(inpt == '*'):
            cricket_menu()
            break
        elif(inpt == '0'):
            MainMenu()
            break
        elif(inpt == '#'):
            exit()
        else:
            print("Please enter correct option")


def football_menu():
    print("""
        Select a particular type:
            1 -> Sport details
            2 -> Legends details
            8 -> Back
            9 -> Exit 
        """)
    while(True):
        try:
            inpt=int(input("Enter an option: "))
            if(inpt==9):
                exit()
            elif(inpt==8):
                MainMenu()
                break
            elif(inpt in range(1,3)):
                # print("passed")
                break
            else:
                print("Please enter valid option: ")
        except Exception:
            print("Please enter valid option: ")   
    football_obj.get_details(inpt)
    print("""   
        Press * to go back
        Press 0 to go to main menu 
        Press # to exit
    """)
    while(True):
        inpt = input("Enter Option: ")
        if(inpt == '*'):
            football_menu()
            break
        elif(inpt == '0'):
            MainMenu()
            break
        elif(inpt == '#'):
            exit()
        else:
            print("Please enter correct option")

def badminton_menu():
    print("""
        Select a particular type:
            1 -> Singles
            2 -> Doubles
            3 -> Default
            4 -> Legend details
            8 -> Back
            9 -> Exit 
        """)
    while(True):
        try:
            inpt=int(input("Enter an option: "))
            if(inpt==9):
                exit()
            elif(inpt==8):
                MainMenu()
                break
            elif(inpt in range(1,5)):
                # print("passed")
                break
            else:
                print("Please enter valid option: ")
        except Exception:
            print("Please enter valid option: ")   
    badminton_obj.get_details(inpt)
    print("""   
        Press * to go back
        Press 0 to go to main menu 
        Press # to exit
    """)
    while(True):
        inpt = input("Enter Option: ")
        if(inpt == '*'):
            badminton_menu()
            break
        elif(inpt == '0'):
            MainMenu()
            break
        elif(inpt == '#'):
            exit()
        else:
            print("Please enter correct option")     
cricket_obj = Cricket() 
football_obj = Football()
badminton_obj = Badminton()
MainMenu() #initially displaying main menu from there we can navigate through other menus



