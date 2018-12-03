import random
names = ["lisa", "bart", "marge", "homer", "maggie"]

def generate_votes(name, numbervotes):
    votes = []
    for i in range(30):
        votes.append(random.choice(names))
    return votes
    
def winner_old(names, votes):
    tallies = {}
    for n in names:
        tallies[n]=0
    print(tallies)
    
    for vote in votes:
        tallies[vote] = tallies[vote]+1
    print(tallies)
    
    max_vote_count = max(tallies.values())
    print(tallies)
    print(max_vote_count)
    
    winners= []
    for k,v in tallies.items():
        if v == max_vote_count:
            winners.append(k)
        print(winners)
    return winners

def winner(names, votes):
    for vote in votes:
        tallies.setdefault(vote, 0)
        tallies[vote] = tallies[vote]+1
    print(tallies)
    
    max_vote_count = max(tallies.values())
    print(tallies)
    print(max_vote_count)
    
    winners= []
    for k,v in tallies.items():
        if v == max_vote_count:
            winners.append(k)
        print(winners)
    return winners
    
votes = generate_votes(names, 30)
    