score_file = open("score.txt", "w", encoding="utf8") # file name, write(overwrite), type
print("math : 0", file=score_file)
print("english : 50", file=score_file)
score_file.close()


score_file = open("score.txt", "a", encoding="utf8") # file name, append, type
score_file.write("science : 80") # write do not have line change. print() automatically adds line change
score_file.write("\ncoding : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r = read
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r = read
print(score_file.readline()) # read every line, after cursor move to next line
print(score_file.readline()) # read every line, after cursor move to next line
print(score_file.readline()) # read every line, after cursor move to next line
print(score_file.readline()) # read every line, after cursor move to next line
score_file.close()

# what if you dont know how long the file is?
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

print()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # bring all the line and save as list
for line in lines:
    print(line, end="")

score_file.close()