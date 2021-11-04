nominee_1 = input("Enter the Nominee 1 Name : ")
nominee_2 = input("Enter the Nominee 2 Name : ")

nom_1_votes = 0
nom_2_votes = 0

votes_id =[1,2,3,4,5,6,7,8,9,10]

num_of_votes = len(votes_id)

while True:
    if votes_id == []:
        print("Voting session OVER")
        if nom_1_votes > nom_2_votes:
            percent = (nom_1_votes/num_of_votes)*100
            print(nominee_1,"has WON with",percent,"% votes")
            break

        elif nom_2_votes > nom_1_votes:
            percent = (nom_2_votes/num_of_votes)*100
            print(nominee_2,"has WON with",percent,"% votes")
            break
    
    else:
        voter = int(input("Enter your voter id number : "))
        if voter in votes_id:
            print("You are a voter")
            votes_id.remove(voter)
            vote = int(input("Enter your vote 1 or 2 : "))
            if vote == 1:
                nom_1_votes += 1
                print("Thank you for casting your vote")
            elif vote == 2:
                nom_2_votes +=1
                print("Thank you for casting your vote")
            else:
                print("You enter wrong number. Please enter either 1 or 2")
        else:
            print("You are not a voter here or you have already voted") 