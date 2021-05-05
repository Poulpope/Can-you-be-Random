d <- Response_file
gramBuffer = list(0,1,0,1,0)
gramHistory = list()
correct = 0
wrong = 0
prediction = 0
lastkey = 0
CorrectCumule= list()
historyIndex = gramBuffer[[1]]*16 + gramBuffer[[2]]*8 + gramBuffer[[3]]*4 + gramBuffer[[4]]*2 + gramBuffer[[5]];
for (i in c(1:64))  { 
  gramHistory[[i]] = 0
}

for (j in c(1:length(d$RESPONSE))) {
  
  if (d$RESPONSE[j] == 'left') {
    lastkey = 0
  } else {
    lastkey = 1
  }
  
  if (prediction == lastkey) {
    correct = correct + 1
    } else {
    wrong = wrong + 1
    }
#counter0 = pair
  gramHistory[[historyIndex*2]] = (1 - lastkey) + gramHistory[[historyIndex*2]]
#counter1 = impair
  gramHistory[[(historyIndex*2)-1]] = lastkey + gramHistory[[(historyIndex*2)-1]]
  
  gramBuffer[[1]] <- gramBuffer[[2]]
  gramBuffer[[2]] <- gramBuffer[[3]]
  gramBuffer[[3]] <- gramBuffer[[4]]
  gramBuffer[[4]] <- gramBuffer[[5]]
  gramBuffer[[5]] <- lastkey
  
  #index de 1 à 32
  historyIndex = gramBuffer[[1]]*16 + gramBuffer[[2]]*8 + gramBuffer[[3]]*4 + gramBuffer[[4]]*2 + gramBuffer[[5]] + 1

  if (gramHistory[[(historyIndex*2)-1]] > gramHistory[[historyIndex*2]]) { 
    prediction = 1
    } else { 
    prediction = 0
    }
  CorrectCumule[[j]] = correct / (correct + wrong)
}
