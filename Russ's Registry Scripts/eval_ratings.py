

file = open('Statistics/All_Ratings.txt', 'r')
lines = file.readlines()

count1 = 0
count0 = 0

for line in lines:
	items = line.split(' ')
	part, rating = items
	if str(1) in rating:
		count1 = count1 + 1
	if str(0) in rating:
		count0 = count0 + 1
	print part + ', ' + rating

print "0 parts: " + str(count0)
print "1 parts: " + str(count1)

