
# started by declaring the variables I will be using
exam = 25
assessment = 15

# this helps the repeat the code
passing = True


while passing: # to accept input of the student's marks since I don't have stored values for each student
    exam_score = float(input("Enter student exam score: "))
    class_score = float(input("Enter student assessment score: "))
    fees = float(input("Enter amount paid for tuition(Enter $100 if paid in full): "))# to make sure students pay their fees
# this is to check that students meet requirement 1 and 2(get 25 plus is exam and 15 plus in class score)
    if exam_score >= exam and class_score >= assessment:
        if fees == 100:# checking if fees have been paid (this condition must be satisfied even if student passed in order to get a certificate)
            print("\n--------You Passed!!---------------")
            print("--------Congratulations!!----------")
            print("You earned a certificate.\n")
        else:
            print("\n--------You Passed!!---------------")
            print("--------Congratulations!!----------")
            print("Pay your fees in full to get a certificate!!\n")
    elif exam_score + class_score == 39: # the condition that a student is condoned on account that he/she gets a total of 39 when exam and class score is added
        if fees == 100:# still checking fee payment to issue certificate
            print("\n--------YOU WERE PARDONED!!--------")
            print("--------Congratulations!!----------")
            print("You earned a certificate.\n")
        else:
            print("\n--------YOU WERE PARDONED!!--------")
            print("--------Congratulations!!----------")
            print("Pay your fees in full to get a certificate!!\n")
# here I single out the requirements to be able to tell the student which requirement he or she failed to meet
    elif exam_score < exam and class_score >= assessment:
        print(f"\nYou need to score at least {exam} to pass the exam!")
        print(f"You scored {exam_score}")
        print("You failed the Exam!\n")

    elif class_score < assessment and exam_score >= exam:
            print(f"\nYou need to score at least {assessment} to pass the assessment!")
            print(f"You scored {class_score}")
            print("You failed the Assessment!\n")
# when student fails to meet both requirements, despite failing It was necessary to point out that he or she was repeated
    elif exam_score < exam and class_score < assessment:
        print("\n-------PAMPAMPAA------")
        print("You failed both the Exam and the Assessment")
        print("You are REPEATED wae!! Kwasiato\n")
# this is to help break out of the loop
    leave = input("Enter (q) to quit, Enter any key to continue: ").lower()
    if leave == "q":
        print("Thank you!!\n")
        break
    else:
        continue

# linking pycharm to GitHub took the time and then the lights went out















