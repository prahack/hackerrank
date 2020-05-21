# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    s = input()
    evenString = ''
    oddString = ''
    for j in range(len(s)):
        if j%2 == 0:
            evenString = evenString + s[j]
        else:
            oddString = oddString + s[j]
    print(evenString + ' ' + oddString)