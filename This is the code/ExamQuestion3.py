# Allows voters to enter either A, B or C.​
# Keeps track of how many times each candidate has been voted for.​
# As soon as one person has finished voting, allows the next person to vote.​
# At any point allows the official to type in “END”, which will print out the number of votes for each candidate and the total number of votes overall.​

voteA = 0
voteB = 0
voteC = 0

while True:
    vote = input("Enter your vote (A, B or C) or type END to finish the vote: ")
    if vote.upper() == "END":
        break
    elif vote.upper() == "A":
        voteA += 1
    elif vote.upper() == "B":
        voteB += 1
    elif vote.upper() == "C":
        voteC += 1
    else:
        print("Invalid input. Please enter A, B, C or END.")

print("Votes:")
print(f"A: {voteA}")
print(f"B: {voteB}")
print(f"C: {voteC}")
print(f"Total: {voteA + voteB + voteC}")