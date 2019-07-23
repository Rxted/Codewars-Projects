'''
The Challenge
In this challenge you will be given a string representing a player's ten frames.
 It will look something like this: 'X X 9/ 80 X X 90 8/ 7/ 44' (in Java: "X X 9/ 80 X X 90 8/ 7/ 44"),
 where each frame is space-delimited, 'X' represents strikes, and '/' represents spares.
 Your goal is take in this string of frames into a function called bowlingScore and return the players total score.
 '''
 
 def bowling_score(frames):
    frameArr = []
    score = 0
    itr = 0
    frameArrRepl = frames.split(" ")
    for i in frameArrRepl:
        for x in i:
            if x=="X":
                frameArr.append("10")
            elif x=="/" and i.index(x) != 2:
                frameArr.append(str(10-int(i[0])))
            elif x=="/":
                frameArr.append(str(10-int(i[1])))
            else:
                frameArr.append(x)
    for i in range(0, len(frameArrRepl)):
        for x in frameArrRepl[i]:
            if x == "X" and i != 9:
                score+=10+int(frameArr[itr+1])+int(frameArr[itr+2])
            elif x == "X" and i == 9:
                score+=10
            elif x == "/" and i != 9:
                score+=10+int(frameArr[itr+1])-int(frameArr[itr-1])
            elif x == "/" and i == 9:
                score+=10-int(frameArr[itr-1])
            else:
                score+=int(x)
            itr+=1
    return score