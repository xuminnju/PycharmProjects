name = input('enter your textbook:')
file = open(name).read()
total = 0
counts = dict()
for line in file:
    line = line.split()
    for letter in line:
        if letter.encode( 'UTF-8' ).isalpha():
            letter = letter.lower()
            counts[letter] = counts.get(letter, 0) + 1
            total +=1
counts = sorted(counts.items(), key=lambda x: x[1], reverse = True)
for letter, count in counts:
    pct = count/total
    print('%s pct is %.2f%%' %(letter, pct*100))
