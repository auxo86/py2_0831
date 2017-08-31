import csv

sampleFile = open('data\\book1.csv')
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)

print type(sampleReader)
print [record for record in sampleData]