# NAME       - RISHU KUMAR
# ENROLLMENT - 0157AL231175
# BATCH      - 5(MTF)
# BATCH TIME - 10:30 - 12:10


## PYTHON SOLUTIONS FOR 40 PROGRAMMING QUESTIONS
##(Basic If–Else)

1.	Positive, Negative, or Zero:
n=int(input())      if=n>0: print("Positive") elif n<0: print("Negative") else: print("Zero")

2.	Even or Odd: 
n=int(input()) print("Even" if n%2==0 else "Odd")

3.	Leap Year: 
year=int(input()) if(year%400==0 or (year%4==0 and year%100!=0)): print("Leap Year") else: print("Not Leap Year")

4.	Greater of Two: 
a=int(input()); b=int(input()) print(a if a>b else b)

5.	Voting Eligibility: 
age=int(input()) print("Eligible" if age>=18 else "Not Eligible")

6.	Vowel or Consonant:
c=input() print("Vowel" if c.lower() in "aeiou" else "Consonant")

7.	Divisible by 5: 
n=int(input()) print("Divisible" if n%5==0 else "Not Divisible")

8.	Digit Category: 
n=int(input()) if -9<=n<=9: print("Single Digit") elif -99<=n<=99: print("Two Digit") else: print("More Than Two Digits")

9.	Pass or Fail: 
marks=int(input()) print("Pass" if marks>=40 else "Fail")

10.	Multiple of 3 and 7:

n=int(input())
print("Yes" if n%3==0 and n%7==0 else "No") 

-(Ladder If / Nested If)

11.	Greatest among 3: 
a,b,c=map(int,input().split()) if a>b and a>c: print(a) elif b>c: print(b) else: print(c)

12.	Age Classification: 

age=int(input()) if age<13: print("Child") elif age<=19: print("Teenager") elif age<=59: print("Adult") else: print("Senior")

13.	Grade: m=int(input()) if 
m>=90: print("A") elif m>=75: print("B") elif m>=50: print("C") elif m>=35: print("D") else: print("Fail") 

14.	Triangle Type: 

a,b,c=map(int,input().split()) if a==b==c: print("Equilateral") elif a==b or b==c or a==c: print("Isosceles") else: print("Scalene")

15.	Character Type:

c=input() if c.isupper(): print("Uppercase") elif c.islower(): print("Lowercase") elif c.isdigit(): print("Digit") else: print("Special Symbol")

16.	Electricity Bill: u=int(input()) if 
u<=100: bill=u*5 elif u<=200: bill=100*5+(u-100)*7 else: bill=100*5+100*7+(u-200)*10 print(bill)

17.	Largest of 4: a,b,c,d=map(int,input().split()) max1=a if a>b else b max2=c if c>d else d print(max1 if max1>max2 else max2)

18.	Century & Leap Year:
y=int(input()) if y%100==0:
    print("Century Year")     print("Leap Year" if y%400==0 else "Not Leap Year") else:     print("Not Century Year")

19.	BMI Classification: bmi=float(input()) if bmi<18.5: print("Underweight") elif bmi<25: print("Normal") elif bmi<30: print("Overweight") else: print("Obese")

20.	Smallest of 3:
a,b,c=map(int,input().split()) if a<b:
    print(a if a<c else c) else:     print(b if b<c else c) (For Loop Problems)

21.	Armstrong (100–999): for n in range(100,1000):
    if sum(int(d)**3 for d in str(n))==n: print(n)

22.	First n Primes:
n=int(input()); count=0; num=2 while count<n:     prime=True     for i in range(2,int(num**0.5)+1):         if num%i==0: prime=False; break     if prime: print(num,end=" "); count+=1     num+=1
23.	Divisible by 3 & digit-sum <=10:
for i in range(1,501):
    if i%3==0 and sum(int(d) for d in str(i))<=10: print(i)

24.	Star Pyramid: n=int(input()) for i in range(1,n+1): print("*"*(2*i-1))

25.	Pangram: s=input().lower() letters=set(c for c in s if c.isalpha()) print("Pangram" if len(letters)==26 else "Not Pangram")


26.	Twin Primes: def prime(n):
    if n<2: return False     for i in range(2,int(n**0.5)+1):         if n%i==0: return False     return True
for n in range(2,101):     if prime(n) and prime(n+2): print(n,n+2)

27.	Harshad: n=int(input()) print("Harshad" if n%sum(int(d) for d in str(n))==0 else "Not Harshad")

28.	Pascal’s Triangle:
n=int(input()) for i in range(n):
    val=1     for j in range(i+1):         print(val,end=" ")         val=val*(i-j)//(j+1)     print()

29.	Sum of Squares: n=int(input()) print(sum(i*i for i in range(1,n+1)))
30.	Strong Number: n=int(input()); s=0 for d in str(n):
    f=1     for i in range(1,int(d)+1): f*=i     s+=f print("Strong" if s==n else "Not Strong") (While Loop Problems)

31.	Reverse & Prime:
n=int(input()); rev=0; x=n while x: rev=rev*10+x%10; x//=10 prime=True for i in range(2,int(rev**0.5)+1:
    if rev%i==0: prime=False print(rev,"Prime" if prime else "Not Prime")

32.	Input until digit-sum>100:
total=0 while total<=100:     num=int(input())
    total+=sum(int(d) for d in str(num)) print("Stopped")

33.	Duck Number:
n=input() print("Duck" if n[0]!="0" and "0" in n else "Not Duck")

34.	Happy Number: n=int(input()) while n!=1 and n!=4:
    n=sum(int(d)**2 for d in str(n)) print("Happy" if n==1 else "Not Happy")

35.	Largest Prime Factor: n=int(input()); mp=-1 while n%2==0: mp=2; n//=2 i=3 while i*i<=n:     while n%i==0: mp=i; n//=i     i+=2
if n>2: mp=n print(mp)

36.	Keep Input Until Palindrome:
while True:     s=input()     if s==s[::-1]: print("Palindrome:",s); break

37.	Digital Root:
n=input() while len(n)>1:
    n=str(sum(int(d) for d in n)) print(n)

38.	Collatz Sequence:
n=int(input()) while n!=1:
    print(n,end=" ")     n=n//2 if n%2==0 else 3*n+1 print(1)

39.	Kaprekar:
n=int(input()); sq=str(n*n); ok=False for i in range(1,len(sq)):
    if int(sq[:i])+int(sq[i:])==n: ok=True print("Kaprekar" if ok else "Not Kaprekar")

40.	ATM Simulation:
bal=1000 while True:
    print("1.Check Balance 2.Deposit 3.Withdraw 4.Exit")     c=int(input())     if c==1: print("Balance:",bal)     elif c==2: bal+=int(input("Amount:"))     elif c==3:
        a=int(input("Amount:"))         print("Insufficient" if a>bal else exec("bal-=a"))     else: break
