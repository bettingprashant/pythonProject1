score = int(input("Enter your score\n"))
Grade = "F"
if score >=90 and score <= 100:
    Grade = "A"
    print("Your grade is ", Grade)
elif score >=80 and score <=89:
    print("Your Grade is ",Grade )
elif score >=70 and score <=79:
    print("Your Grade is ",Grade)
elif score >= 60 and score <= 69:
    print("Your Grade is ",Grade)
elif score >100:
    print("You are Genius ")
else:
    Grade = "F"
    print("Your grade is", Grade)