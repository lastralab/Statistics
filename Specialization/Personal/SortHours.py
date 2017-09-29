name = "mail.txt"
counts = dict()
handle = open(name)
for line in handle:
     line = line.rstrip()
     if line == '':
          continue
     words = line.split()
     if words[0] == 'From':
          counts[words[5][:2]] = counts.get(words[5][:2], 0) + 1
        
tlist = list()
for key, value in counts.items():
      newtup = (key, value)
      tlist.append(newtup)


tlist.sort()


for key, value in tlist:
      print key, value
