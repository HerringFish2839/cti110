# Test Average and Grade
# 6/17/17
# CTI-110 M5HW1 - Test Average and Grade
# Bryce Herring
#

#Calculates the average.
def calc_average(score1, score2, score3, score4, score5 ):
    Average = ( score1 + score2 + score3 +score4 + score ) / 5
    return Average

#Determines the user's grade.
def determine_grade( user_score ):
    if( user_score < 60):
        return "F"
    elif( user_score < 70 ):
        return "D"
    elif(user_score < 80 ):
        return "C"
    elif(user_score < 90 ):
        return "B"
    else:
        return "A"

#Asks the user for five scores.
def Ask_Score():
    score1 = float( input( "Please enter score 1: ") )
    score2 = float( input( "Please enter score 2: ") )
    score3 = float( input( "Please enter score 3: ") )
    score4 = float( input( "Please enter score 4: ") )
    score5 = float( input( "Please enter score 5: ") )

    return score1, score2, score3, score4, score5

#Prints the results of the scores.
def Results(score1, score2, score3, score4, score5):
    print( "Score\tLetter Grade\n" )
    print( str( score1 ) + "\t" + determine_grade( score1 ), \
           str( score2 ) + "\t" + determine_grade( score2 ), \
           str( score3 ) + "\t" + determine_grade( score3 ), \
           str( score4 ) + "\t" + determine_grade( score4 ), \
           str( score5 ) + "\t" + determine_grade( score5 ), sep = "\n" )

#Prints out the asked scores and the results of those scores.
def main():
    score1, score2, score3, score4, score5 = Ask_Score()
    print()
    Results( score1, score2, score3, score4, score5 )

main()
