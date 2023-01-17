import csv

# Initialize variables

total_votes = 0
candidate_list = []
candidate_votes = {}

#import CSV

file_import = "/Users/bennettnorthcutt/Module 3/python-challenge/PyPoll/Resources/election_data.csv"

# loop through CSV

with open(file_import) as file:
    
    csv_read = csv.reader(file, delimiter=",")
    next(csv_read)
    
    #loop through all of the rows
    for row in csv_read: 
        total_votes += 1
        candidate = row[2]
        
        # Check to see if candidate is already recorded
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] =  0
            
        #count candidate votes 
        candidate_votes[candidate] += 1
            
 #identify winner by number of votes   
winner = max(candidate_votes, key=candidate_votes.get)


#Print Results

print("Election Results")
print( "-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#Print Candidate Information
for candidate, votes in candidate_votes.items():
    percentage = round(votes / total_votes * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")

print( "-------------------------")
print(f"Winner: {winner}")
print( "-------------------------")



#Save to Txt 

with open("PyPoll Output - Module 3", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write( "-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = round(votes / total_votes * 100, 3)
        text_file.write(f"{candidate}: {percentage}% ({votes})\n")

    text_file.write( "-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write( "-------------------------\n")
    
    

