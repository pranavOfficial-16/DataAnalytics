# read file
import os.path

f = open("../Data/funny.txt", "r")
for line in f:
    print(line)
f.close()

# with statement
with open("../Data/funny.txt", "r") as f:
    for line in f:
        print(line)

# readlines()
with open("../Data/funny.txt", "r") as f:
    lines = f.read()
    print(lines)

# write file
with open("../Data/funny.txt", "w") as f:
    f.write("I love python")

# same file when you write i love javascript the previous line goes away
with open("../Data/love.txt", "w") as f:
    f.write("I love python")

# You can use append mode to stop having previous lines overwritten
with open("../Data/love.txt", "a") as f:
    f.write("I love python")

# writelines
with open("../Data/love.txt", "w") as f:
    f.writelines(["I love C++\n", "I love scala"])

# program to perform data analytics on cricket player's performance
player_scores = {}
with open("../Data/scores.csv", "r") as f:
    for line in f:
        player,score = line.split(',')
        score = int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

print(player_scores)

for player, score_list in player_scores.items():
    min_score = min(score_list)
    max_score = max(score_list)
    avg_score = sum(score_list) / len(score_list)

    print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg:{avg_score}")

if os.path.exists("../Data/cost.txt"):
    print("true")

with open("../Data/cost.txt","w") as savedFile:
    savedFile.write("Hey man whats up!")
