# DPC 106 [E]
# Random Talker, Part 1

cap0 = "QWERTYUIOPASDFGHJKLZXCVBNM"
low0 = "qwertyuiopasdfghjklzxcvbnm"
cap,low = [], []
for k in cap0:
    cap += [k]
for k in low0:
    low += [k]

wordlist = []
wordcount = []
wordenders = [" ", "\n", ".", ",", ":", ";", "!", "?", "(", ")", "[", "]", "{", "}"]

dpcfo = open("dpc106easytext.txt","r")

S = dpcfo.read()

currentword = ""
for k in S:
  if (k not in wordenders):
    if (k in cap):
        jcap = cap.index(k)
        k = low[jcap]
    currentword += k
  else:
    if (currentword != ""):
      if (currentword in wordlist):
        j = wordlist.index(currentword)
        wordcount[j] += 1
      else:
        wordlist += [currentword]
        wordcount += [1]
      currentword = ""
    if (k != " " and k != "\n"):
      if (k in wordlist):
        j = wordlist.index(k)
        wordcount[j] += 1
      else:
        wordlist += [k]
        wordcount += [1]
    else:
      thisline = "filler"


sortword = []
sortcount = []


while (len(sortcount) < 10):
  top = max(wordcount)
  jtop = wordcount.index(top)
  sortword += [wordlist[jtop]]
  sortcount += [wordcount[jtop]]
  del wordlist[jtop]
  del wordcount[jtop]

for k in range(0,len(sortcount)):
  print sortcount[k], sortword[k]

quitprogram = raw_input("anykey to quit")
