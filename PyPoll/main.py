# Import Dependencies
import os
import csv

# Set path for csv file
path_csv=os.path.join("PyPoll","Resources","election_data.csv")

total_votes=0
candidate_dict={}
candidates=[]
number_votes=[]
vote_percent=[]


# skip the header
with open(path_csv,"r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)

# The total number of votes cast

    for row in csv_reader:
        total_votes+=1

# Candidate list & vote counts
        
        if row[2] in candidate_dict.keys():
            candidate_dict[row[2]]=candidate_dict[row[2]]+1
        else:
            candidate_dict[row[2]]=1

    for key, value in candidate_dict.items():
        candidates.append(key)  # candidate name
        number_votes.append(value) # vote for each candidate


# Vote percentage calculation
        
    for n in number_votes:
        vote_percent.append(round(n/total_votes*100,3))  
    print(f"\n")
    print("Election Result\n")
    print(f"------------------------------\n")
    print(f"Total votes : {total_votes}\n")
    print(f"------------------------------\n")

    count = 0
    for key, value in candidate_dict.items():
        for percent, candidate in zip(vote_percent, candidate_dict):
            print(f"{candidate} : {percent}% ({number_votes[count]})")
            count=count+1
        break

    print("-----------------------------------")    
    candidate_max=max(zip(candidate_dict.values(),candidate_dict.keys()))
    print(f"Winner:  {candidate_max[1]}")
    print("-----------------------------------") 


 

