'''
Create a class Player with below attributes:

playerId - int
playerName - String
runs - int
playerType - String
matchType - String

write constructor as required. 

Create class Solution with main method. 

Implement two static methods - 
findPlayerWithLowestRuns and 
findPlayerByMatchType in Solution class.

findPlayerWithLowestRuns method:
This method will take array of Player 
objects and a String value as input 
parameters.
The method will return the least runs 
of the Player from array of Player 
objects for the given player type.
(String parameter passed). If no Player 
with the above condition are present in 
array of Player objects,
then the method should return 0.

findPlayerByMatchType method:
This method will take array of Player 
objects and String value as input parameters 
and return the array of Player objects
belonging to the match type passed as 
input parameter in Descending order of 
playerId.
If no Player with the above condition are 
present in the array of Player objects, 
then the method should return null.

Note : No two Players will have the same 
playerId and runs.
All the searches should be case insensitive.

The above mentioned static methods should 
be called from the main method. 

For findPlayerWithLowestRuns  method - The 
main method should print the returned runs 
as it is
if the returned value is greater than 0 or 
it should print "No such player".

Eg: 25
where 25 is the lowest runs of the Player.

For findPlayerByMatchType method - The main 
method should print the playerId from the 
returned Player array for each
Player if the returned value is not null. 
If the returned value is null then it should 
print "No Player with given matchType".


Eg:
13
11
where 13 and 11 are the playerId's.

Before calling these static methods in 
main, use Scanner object to read the values 
of four Player
objects referring attributes in the above 
mentioned attribute sequence. 
Next, read the value of two String parameter 
for capturing player type and match Type.

Consider below sample input and output:

Input1:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
State
One day

Output:
67
14ccccc
11


Input2:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
District
T20


Output:
No such player
No Player with given matchType



'''


'''
class Player:
    def init(self, playerId, playerName, runs, playerType, matchType):
        self.playerId = playerId
        self.playerName = playerName
        self.runs = runs
        self.playerType = playerType
        self.matchType = matchType
class Solution:
    def findPlayerWithLowestRuns(players, playerType):
        filtered_players = [player.runs for player in players if player.playerType.lower() == playerType.lower()]
        if filtered_players:
            return min(filtered_players)
        else:
            return 0

    def findPlayerByMatchType(players, matchType):
        filtered_players = [player for player in players if player.matchType.lower() == matchType.lower()]
        if filtered_players:
            sorted_players = sorted(filtered_players, key=lambda x: x.playerId, reverse=True)
            return [player.playerId for player in sorted_players]
        else:
            return None

# Read the input values
players = []
for _ in range(4):
    playerId = int(input())
    playerName = input()
    runs = int(input())
    playerType = input()
    matchType = input()
    player = Player(playerId, playerName, runs, playerType, matchType)
    players.append(player)
playerType = input()
matchType = input()

# Call the findPlayerWithLowestRuns method
lowestRuns = Solution.findPlayerWithLowestRuns(players, playerType)

# Print the lowest runs or "No such player"
if lowestRuns > 0:
    print(lowestRuns)
else:
    print("No such player")

# Call the findPlayerByMatchType method
playersByMatchType = Solution.findPlayerByMatchType(players, matchType)

# Print the playerIds or "No Player with given matchType"
if playersByMatchType:
    for playerId in playersByMatchType:
        print(playerId)
else:
    print("No Player with given matchType")

'''




class Player:
    def __init__(self,pid,pn,r,pt,mt):
        self.pid=pid
        self.pn=pn
        self.r=r
        self.pt=pt
        self.mt=mt
class Solution:
    
    @staticmethod
    def findPlayerWithLowestRuns(plist,pt): 
        rl=[p.r for p in plist if p.pt.lower()==pt.lower()]
        if rl:
            print(min(rl))
        else:
            print("1.no")
    def findPlayerByMatchType(plist,mt):
        pl=[]
        for p in plist:
            if p.mt==mt:
                pl.append(p)
        pl=sorted(pl,key=lambda x:x.pid)
        if pl==[]:
            print("2.no")
        else:
            for x in pl:
                print(x.pid)

# n=int(input())
plist=[]
for i in range(4):
    pid=int(input())
    pn=input()
    r=int(input())
    pt=input()
    mt=input()
    play=Player(pid,pn,r,pt,mt)
    plist.append(play)
pt=input()
mt=input()
Solution.findPlayerWithLowestRuns(plist,pt)
Solution.findPlayerByMatchType(plist,mt)


        