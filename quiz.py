import random

def funtion_question(index)->str:
    
     questions = [
                "Chief Election Commissioner of India is appointed by:",
                "Under which of the following provisions is the Booth Level Officer (BLO) appointed?",
                "What actions can be taken by the Electoral Registration Officer (ERO) with reference to the Electoral Roll?",
                "What is the maximum age prescribed for registration in the electoral roll?",
                "Which form number is prescribed for the inclusion of name in the electoral roll as an overseas elector?",
                "In NCT of Delhi, electoral rolls are maintained?",
                "What is the maximum permissible limit of distance normally for voters to reach his/her polling station?",
                "In case of a lost EPIC (Voter ID Card), a duplicate EPIC can be issued on payment of the prescribed fee of Rs. _?",
                "Booth Level Agents can be appointed by?",
                "How many maximum candidates can be set in one ballot unit?",
                "The Counting of voters is done by using?",
                "The EVM is closed at the end of the poll by:",
                "EVM after polling and before counting is kept in:",
                "The last part of the electoral roll:",
                "EPIC does not contain:",
                "The Indian Parliament consists of the following Houses:",
                "Which of the following is essential for being eligible to cast a vote?",
                "Who is responsible for the preparation of the Electoral Roll?",
                "For how many years, an MLA is elected?",
                "What is the total number of seats in Lok Sabha?",
                "Symbols to the political parties at the time of the election are allotted by:",
                "Which of the following categories of voters is entitled to vote by post?",
                "Which authority conducts elections to the offices of the President and Vice-President of India?",
                "Which authority conducts elections to Parliament?",
                "What is the full form of NOTA?"
               ]
     return questions[index]


def funtion_answer(index) ->list:
    
    answers = [
                    ["(A) UPSC", "(B) Prime Minister of India", "(C) President of India", "(D) None of the above"],
                    ["(A) Section 13 B (2) of the Representation of the People Act, 1950.", "(B) Section 13 CC of the Representation of the People Act, 1950.",
                    "(C) Section 26 of the Representation of the People Act, 1950.", "(D) Rule 14 of the Registration of Electors Rules, 1960."],
                    ["(A) Addition", "(B) Deletion", "(C) Correction", "(D) All of the above."],
                    ["(A) 80 years", "(B) 90 years", "(C) 100 years", "(D) No limit"],
                    ["(A) Form -6", "(B) Form -8", "(C) Form -6A", "(D) Form -8A"],
                    ["(A) Parliamentary Constituencies wise", "(B) Assembly constituencies wise", "(C) Both a & b", "(D) None of the above."],
                    ["(A) Upto 1 KM", "(B) Upto 2 KM", "(C) Upto 3 KM", "(D) Upto 4 KM"],
                    ["(A) 10/-", "(B) 25/-", "(C) 50/-", "(D) 75/-"],
                    ["(A) Returning Officer (RO)", "(B) District Election Officer (DEO)", "(C) Political Party", "(D) MLA"],
                    ["(A) 24", "(B) 16", "(C) 28", "(D) 32"],
                    ["(A) Ballot Unit", "(B) Control Unit", "(C) Both A & B", "(D) Any of the above"],
                    ["(A) Candidate", "(B) Returning Officer", "(C) ERO", "(D) Polling Officer in charge"],
                    ["(A) RO Office", "(B) ERO Office", "(C) Strong Room", "(D) ECI Office"],
                    ["(A) Is concerned with the addition supplement", "(B) Is for electors who hold a declared office.",
                    "(C) Is concerned with service electors.", "(D) Is concerned with those electors who have appointed a proxy electors on their behalf."],
                    ["(A) Facsimile signature of ERO", "(B) Hologram", "(C) Elector’s Photograph", "(D) Facsimile signature of DEO"],
                    ["(A) Only Lok Sabha", "(B) Only Rajya Sabha", "(C) Lok Sabha and Rajya Sabha", "(D) None of these"],
                    ["(A) Having EPIC", "(B) Having passport", "(C) Having ration card", "(D) Having name enrolled in electoral roll."],
                    ["(A) RO", "(B) AERO", "(C) ERO", "(D) BLO"],
                    ["(A) 04 years", "(B) 05 years", "(C) 06 years", "(D) 07 years"],
                    ["(A) 555", "(B) 535", "(C) 545", "(D) 575"],
                    ["(A) Election Commission of India.", "(B) CEO of the State.", "(C) Returning Officer.", "(D) District Election Officer."],
                    ["(A) Service voters", "(B) General Voters", "(C) Overseas voters", "(D) None of the above"],
                    ["(A) Parliament", "(B) Supreme Court", "(C) Election commission of India(ECI)", "(D) State election commission"],
                    ["(A) Parliament", "(B) Election Commission of India (ECI)", "(C) Supreme Court", "(D) State Election Commission"],
                    ["(A) None of those above", "(B) None of these above", "(C) None of the above", "(D) Not of the above"]
                ]
    return answers[index]
    
    
    
def funtion_correct_option(index) -> str:
    correct_options= [
                "C", "A", "D", "D", "C",#q1-5 
                "B", "B", "B", "C", "B",#q6-10 
                "B", "D", "C", "C", "D",#q11-15
                "C", "D", "C", "B", "C",#q16-20
                "A", "A", "C", "B", "C"#q21-25
            ]
    return correct_options[index]
    
def random_values()-> int  :
    numbers = random.sample(range(25), 25)
    for i in range(1, 2):
        random_number= numbers[i % 25]
    return random_number    
    
 #TODO: random orderly questions and avoid reptation
#todo : set timer 
def main()->None:
    choices:set=("A","B","C","D")
    print("welcome")
    grade=0
    for index in range(1,4):
        #print(random_values())
        random_value =random_values()
        print(f"{index}.{funtion_question(random_value)}")
        #print(funtion_question(random_value))
        #for ans in funtion_answer(index):
        answers = funtion_answer(random_value)
        for answer in answers:
            print(answer)
        options = input().capitalize()[0]
        attempt = 0
        while options not in choices:
            attempt+=1
            print("You Entered wrong option, Enter only",choices)
            options = input().capitalize()[0]
            
            if attempt == 2 :
                break
            else:
                print() 
            #TODO: end the tries after 3 times, move to next questions
        print("You Entered option:",options) 
        if funtion_correct_option(random_value) == options:
            print("correct")
            grade +=1
            print(grade)
        else:
            print("incorrect")
    print("marks are:",grade)

    
if __name__ == "__main__":
    main()
   

   
    