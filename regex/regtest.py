import re


def Main():
	line = "I think I understand regular expressions"
	matchResult = re.match('think', line, re.M|re.I)
	if matchResult:
		print "Match found: " + matchResult.group()
	else:
		print "No match found"
	
	searchResult = re.search('think', line, re.M|re.I)
        if searchResult:
                print "Search found: " + searchResult.group()
        else:
                print "No search found"

        text1 = 'Title</h1><p>This is a<a href="http://www.udacity.com">link</a>'
	text = '<a href="http://www.udacity.com">link'
        searchResultText = re.findall('<[\sA-za-z0-9\/=:\"\.]+>', text) 

        if searchResultText:
                print "search text found: "
		print searchResultText
        else:
                print "No search text found"

        text_sub = "<h1>Title</h1><p>This is a"
        replaced = re.sub('<[\sA-za-z0-9\/=:\"\.]+>', ' ', text)
#        print replaced
#	print replaced.split()
 
if __name__ == '__main__':
	Main()
