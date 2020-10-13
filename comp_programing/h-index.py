"""

Input

2

3
5 1 2

6
1 3 3 2 2 15

Output

Case #1: 1 1 2
Case #2: 1 1 2 2 2 3

"""

# inicialize
#Ntests = input()
#i = 1

#while(i != Ntests):

# input
Npapers = 0
Ncitations = []
Npapers = input()  # Npapers is the number of papers
#Ncitations = input()  # Ncitations is the number of citations
h = 0  # we start with h = 0

# DO STUFFF
k = 0
for k in range(0, Npapers - 1):
    print("Case #")

    if Ncitations[k] == 0:
        pass

    if Ncitations[k] > 0:
        if Ncitations[k] > k:
            h = h + 1
            print(h)
        else:
            pass

#i = i+1








