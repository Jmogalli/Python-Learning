# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        float(count)
        t = line.find('0')
        n = float(line[t:])
        total = total + n
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
Average = total / count
print('Average spam confidence:', Average)
