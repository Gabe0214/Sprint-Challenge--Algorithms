'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: # base case
        return 0
    ## see if the first two words contains th
    else:
        if word[0:2] == 'th':
            return 1 + count_th(word[2:])  ## recursion occurs with the th removed to calculate more th within the word
        else:
            ## This is saying that the following letter will be removed, so that the search for th continues.
           return count_th(word[1:])



    # TBC
    

