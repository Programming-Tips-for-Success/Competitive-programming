
def brute_force_match(word, text):
    m = len(word)
    n = len(text)

    counter = 0

    for i in range(0,n-m+1):
        found = True
        for j in range(0, m):
            if word[j] != text[i+j]:
                found = False
                break
        if found: 
            counter += 1
            print(i)

    if counter == 0:
        print( "No match")
    else:
        print( "The word appears: ",counter, "times!")

brute_force_match("ABC","ABCDABCEABC") 
