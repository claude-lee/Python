import re


def Main():
	line = "I think I understand regular expressions"
	matchResult = re.match(r'think', line, re.M|re.I)
	if matchResult:
		print "Match found: " + matchResult.group()
	else:
		print "No match found"
	
	searchResult = re.search(r'think', line, re.M|re.I)
        if searchResult:
                print "Search found: " + searchResult.group()
        else:
                print "No search found"

if __name__ == '__main__':
	Main()
