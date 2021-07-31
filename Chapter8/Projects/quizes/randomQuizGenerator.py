'''
Creates 35 different quizzes.
Creates 50 multiple-choice questions for each quiz, in random order.
Provides the correct answer and three random wrong answers for each
question, in random order.
Writes the quizzes to 35 text files.
Writes the answer keys to 35 text files.
'''
'''Must Generate random questions along side their asnwer key'''
import random

# The quiz data.Keys are states and valuers are thier capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# %s is used to add string within a string 
# is used to add values withing the string.
# can be used to edit outside 
# makes code smaller and cleaner

#Generate 35 quiz files
for quizNum in range(35):                                                               # for file quiznum repeated 35 times
    # TODO: Create the quiz and answer key files.                       
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')                         # create files called capitalquiz%s.txt the %s is reprlaced with the number string        
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')             # the same applies from above but just the answers
    
    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')                                    # Create String placeholders for Appeal test
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))        # Create the header for each individual test
    quizFile.write('\n\n')                                                              # create new lines
    
    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())                                                      # shuffle the states
    random.shuffle(states)
    
    # TODO: Loop though all 50 states, making a question for each. 
    for questionNum in range(50):                                                       # for file qusetionNum repeated 50 times
        # get right and wrong asnwers                                                   # each question will have the following
        correctAnswer = capitals[states[questionNum]]                                   # the correct answer is the value of capitals from list of states within the questionNum
        wrongAnswers = list(capitals.values())                                          # Creating a variable wrong aswers and gets random state question from the list
        del wrongAnswers[wrongAnswers.index(correctAnswer)]                             # delete the correct aswer from the wrong answer
        wrongAnswers = random.sample(wrongAnswers, 3)                                    # Create 3 random wrong answers 
        answerOptions = wrongAnswers + [correctAnswer]                                   # Crate the multiple choice answer 
        random.shuffle(answerOptions)                                                    # shuffle the postion where the right asnwer will be 

    # TODO: write the question and answer option to the quiz file
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))              # Create the number of question with the string and values from questionNum
    for i in range(4):                                                                                      # Create answer options 4 times
        quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))                                          # create list of the question
    quizFile.write('\n')                                                                                    # seperate the question with a line
    
    
    #TODO: write the asnwer key to a file.
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))           # write the question and display the correct asnwer for the answerkeyfile
quizFile.close()                                                                                            # close the quiz file
answerKeyFile.close()                                                                                       # close the answer key file 