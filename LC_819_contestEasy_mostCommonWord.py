#https://leetcode.com/contest/weekly-contest-80/problems/most-common-word/




# first format paragraph replacing all punctuation with " " then split on " " to get the valid words
def mostCommonWord(paragraph, banned):
    temp = list(paragraph)
    for i in range(0,len(paragraph)):
        if temp[i] in ("!","?","'",",",";","."):
            temp[i] = " "
    temp = "".join(temp)
    
    paragraph = temp.split(" ")
    dp = {}
    
    running_max = 0

    # now that paragraph is formatted better, we just keep track of the word counts for words (all mapped to lowercase) and return the most frequent unbanned word
    for word in paragraph:
        if word == "":
            continue
        word = word.lower()   
        if word in dp:
            dp[word] += 1
        else:
            dp[word] = 1
        if word not in banned:
            if dp[word] > running_max:
                running_max = dp[word]
                answer = word
    return answer