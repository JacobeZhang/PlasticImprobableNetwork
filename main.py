import csv
import random

montecarlo = 0
counter = 0
trumpwin = 0
bidenwin = 0

"""
Gradings from FiveThirtyEight:
b,b,b-,b-,b-,b-,b,c-,c+,b+,a/b,a/b,b/c,b/c,b/c,a,b/c,b/c,b

The Polls:
YouGov, YouGov, Research Co., Ipsos, Ipsos, Ipsos, YouGov, YouGov, Change Research, Rasmussen Reports/Pulse Opinion Research, Quinnipiac University, IBD/TIPP, IBD/TIPP, USC Dornsife, USC Dornsife, USC Dornsife, SurveyUSA, RMG Research, Morning Consult, YouGov, Prof. Allan Lichtman"""

def ElectionSimulation(PollGrades):
  trump = 0
  biden = 0
  x = 0
  skip = 0
  counter = 0
  while counter != 18:
    with open('ElectionPred.csv', newline="\n")as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in spamreader:
        for j in row:
          if skip / 2 == 0:
            skip += 1
            x = j
          else:  
            randomnumber = random.randrange(100)
            if int(j) >= randomnumber:
              trump += 1 * (int(PollGrades[str(counter)]) / 100)
            elif 100-int(x) <= randomnumber:
              biden += 1 * (int(PollGrades[str(counter)]) / 100)
            skip += 1
      counter += 1
  if trump > biden:
    return "trumpwin"
  elif trump < biden:
    return "bidenwin"

PollGrades = {
  "0" : "85",
  "1" : "85",
  "2" : "82",
  "3" : "82",
  "4" : "82",
  "5" : "82",
  "6" : "85",
  "7" : "72",
  "8" : "77",
  "9" : "87",
  "10" : "90",
  "11" : "90",
  "12" : "80",
  "13" : "80",
  "14" : "80",
  "15" : "95",
  "16" : "80",
  "17" : "80",
  "18" : "85",
  "19" : "100"
}

while montecarlo != 1000:
  if ElectionSimulation(PollGrades) == "trumpwin":
    trumpwin += 1
  elif ElectionSimulation(PollGrades) == "bidenwin":
    bidenwin += 1
  montecarlo += 1
print("Trump won", trumpwin, "times")
print("Biden won", bidenwin, "times")