'''
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling on a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like
 



So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :
Window Seat: WS
Middle Seat: MS
Aisle Seat: AS
You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.
INPUT
The first line of input will consist of a single integer T denoting the number of test-cases. Each test-case consists of a single integer N denoting the seat-number.
OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.
CONSTRAINTS
1<=T<=105
1<=N<=108
SAMPLE INPUT  
2
18
40
SAMPLE OUTPUT  
19 WS
45 AS
 
PYTHON PROGRAM
'''
a = input()
N = []
for i in range(int(a)):
    b = int(input())
    N.append(b)
s = 'WS'
middle = "MS"
aisle ='AS'
sx = str(s)
middleSeat = str(middle)
aisleseat = str(aisle)
for i in range(len(N)):
       if(N[i]%6==0 or N[i]%6==1):
           if(N[i]%12==0):
               print('{0} {1}'.format(N[i]-11, sx))
           elif(N[i]%12==1):
               print('{0} {1}'.format(N[i]+11, sx))
           elif(N[i]%6==0):
               print('{0} {1}'.format(N[i]+1, sx))
           else:
               print('{0} {1}'.format(N[i]-1, sx))
       elif((N[i]-2)%3==0):
           if(N[i]%12==2):
               print('{0} {1}'.format(N[i]+9, middleSeat))
           elif((N[i]-3)%12==2):
               print('{0} {1}'.format(N[i]+3, middleSeat))
           elif((N[i]-6)%12==2):
               print('{0} {1}'.format(N[i]-3, middleSeat))
           else:
               print('{0} {1}'.format(N[i]-9, middleSeat))
       else:
           if((N[i]-3)%12==0):
               print('{0} {1}'.format(N[i]+7, aisleseat))
           elif(N[i]%12==4):
               print('{0} {1}'.format(N[i]+5, aisleseat))
           elif(N[i]%12==9):
               print('{0} {1}'.format(N[i]-5, aisleseat))
           else:
               print('{0} {1}'.format(N[i]-7, aisleseat))

# Stay tuned for next coding Problems Solution!!!!