def eligible_for_vote(vote):
    if age >= 18 :
        print("You are eligible for Voting")
    else :
        print("You are not eligible")

age = int(input("Enter the Age for Voting"))
eligible_for_vote(age)
