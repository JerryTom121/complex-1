import csv;

# tweet data
csvFile='/home/ivan/Downloads/twitterSentimentData/training.1600000.processed.noemoticon.csv';


with open(csvFile, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print row[0],row[5];
        print ' '.join(row);
        break;