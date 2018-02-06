import pandas as pd

#originally ran with both sets of data; defined both and included both into frame
df=pd.read_csv("election_data_1.csv") 

frame = [df]

election_result = pd.concat(frame)

total_votes = election_result.shape[0]

election_result.groupby(["Candidate"]).size()

candidate_count= election_result.groupby(["Candidate"]).size()

winner = candidate_count.idxmax()

candidate_percent = round(candidate_count/total_votes * 100, 0)

candidate_percent=candidate_percent.astype(str)

for i in range(len(candidate_percent)):
    candidate_percent[i]=candidate_percent[i]+"%" 

#can add +str(candidate_count) to print statement if want to display as well
with open('ElectionResults.txt','w') as f:  
    print("Election Results\n-----------------------\n"+"Total Votes:"+str(total_votes)+"\n-----------------------\n"+str(candidate_percent)+"\n-----------------------\n"+"Winner:"+str(winner)+"\n-----------------------\n", file=f)