# coding=utf8

import re

regex = r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{4}|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}={2})$"

'''
test_str = ("ThisIsNotBase64Because/ItIsNotMod4\n"
	"ThisIsBase64Because/ItIsMod4\n"
    "aGVsbG8gd29ybGQ=\n"
	"ThisIsAlso/Base64+EvenWithPadding+==\n"
	"ThisIsNotBase64+Because-ThereIsADash\n"
	"YouGetTheIdea/==")
'''

test_str1 = input("Enter something \n")

matches = re.finditer(regex, test_str1, re.MULTILINE)

for matchNum, match in enumerate(matches):
    
    print ("Match {matchNum} was found: {match}".format(matchNum = matchNum, match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found : {group}".format(groupNum = groupNum, group = match.group(groupNum)))
