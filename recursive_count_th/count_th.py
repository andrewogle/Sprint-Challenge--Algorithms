'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    th = 0 
    if len(word) < 2 :
        return 0
    if word[-2:] == 'th' :
        th +=1
    return th + count_th(word[:len(word)-1])
