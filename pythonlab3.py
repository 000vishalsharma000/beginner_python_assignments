import math

#1
# equation : ax^2 + bx + c =0
def quadratic_roots():
    a=int(input("enter the value of a : "))
    b=int(input("enter the value of b : "))
    c=int(input("enter the value of c : "))

    discriminant= ((b**2) - (4*a*c))

    if discriminant<0:
            print("roots are imaginary")
            d=abs(discriminant)
                
            print(f'''
            root1 is {-b} + {math.sqrt(d/(2*a))}i
            root2 is {-b} - {math.sqrt(d/(2*a))}i
            ''')

    else :
        root1= (-b + math.sqrt(discriminant/(2*a)))
        root2= (-b - math.sqrt(discriminant/(2*a)))



        if discriminant==0:
                print("both roots are equal")
                print(f'''
                root1 is {root1}
                root 2 is {root2}
                ''')

        elif discriminant>0:
                print(f'''
                root1 is {root1}
                root 2 is {root2}
                ''')              
        
quadratic_roots()

#2
def solve_2var_linear_equations():
    print('''
    for equations...
    ax + by=e
    cx + dy=f
    ''')

    a= int(input("enter the value of a : "))
    b= int(input("enter b : "))
    c= int(input("enter c : "))
    d= int(input("enter d : "))
    e= int(input("enter e : "))
    f= int(input("enter f : "))

    d=(a*d)-(b*c)
    dx= (d*e)-(f*b)
    dy=(a*f)-(c*e)

    if(d==0):
        print("no solution ")
    else:
        print(f"""
        x = {dx/d}
        y = {dy/d}
        """)    

solve_2var_linear_equations()


#3
import random

def guess_sum():
    guess= int(input("guess sum of two nums between 0-100"))
    num_1= random.randint(0,101)
    num_2= random.randint(1,101)
    sum= num_1 + num_2
    if(guess==sum):
        print("your guess is correct")
    else:
        print("your guess is incorrect")
        print(f'correct number was {sum}')
    

guess_sum()

#4
def future_day():
    days={
        0:"sunday",
        1:"monday",
        2:"tuesday",
        3:"wednesday",
        4:"thrusday",
        5:"friday",
        6:"saturday"
    }

    # key_li= [d for d in days ] # these are called list comprehensions , it will return list of keys 
    # val_li= [days[i] for i in days ] # list comprehension , it willl return list of values in dictionary
    k_lst=list(days.keys())
    v_lst=list(days.values())

    day=int(input("enter day no of todays day"))
    no_of_days= int(input("enter no days left for future day"))
    nxt_day_no= (day+no_of_days)%7

    print(f" day after  {no_of_days}  of days after {days[day]} is {days[nxt_day_no]}")

future_day()

#5
def best_rice_packet():
    wt_pr_pair={}
    wt_by_pr_lst=[]
    i=1
    while(True):
        print("enter -ve price,weight to stop ")
        
        weight = int(input(f"eneter the weight of rice packet {i} "))

        if(weight<0 ):
            break

        price = int(input(f"eneter the price  of rice packet {i} "))

        if(  price<0):
            break
        
        wt_pr_pair[i-1]=[weight, price]
        wt_by_pr_lst.append(weight/price)
        i+=1


    wt_by_pr_lst.sort( reverse=True)   #we can also use max(wt_by_pr_lst) OR wt_by+pr_lst[-1]
    max_wt_by_pr=wt_by_pr_lst[1]       # to get max element in it without sorting it

    
    pkt_lst=[w+1 for w,p in wt_pr_pair.items() if (p[0]/p[1]) == max_wt_by_pr ]


    print("packets with best value for money are " , pkt_lst )


best_rice_packet()

#6
def days_in_month_of_year():
    monthName_monthNum_days={
        "january":[1,31],
        "february": [2,28],
        "march":[3,31],
        "april": [4,30],
        "may":[5,31],
        "june": [6,30],
        "july":[7,31],
        "august": [8,31],
        "september":[9,30],
        "october": [10,31],
        "november":[11,30],
        "december": [12,31]
    }

    key_lst=list(monthName_monthNum_days.keys())

    def is_leap_year(year):
        if year%4==0 and year%100!=0:
            return True 
        if year%100==0 and year%400==0:
            return True
        return False

    month=input("enter the month name : ")
    formatted_month_name=month.strip().lower()

    if(formatted_month_name not in key_lst):
        print( "please enter valid month name")

    else :
        year=int(input("enter the year : "))
        month_num=monthName_monthNum_days[formatted_month_name][0]
        if(is_leap_year):
            print(f"{year} is a leap year")

        if(month_num==2 and is_leap_year):
            print(f"there are {monthName_monthNum_days[formatted_month_name][1] + 1} day in {month} of year {year} ")
        else:
            print(f"there are {monthName_monthNum_days[formatted_month_name][1]} day in {month} of year {year} ")



days_in_month_of_year()

#7
def divisibility_by_five_six():
    num=int(input(f"enter a number : "))
    if num%5==0 and num%6==0:
        print(f"{num} is divisible by both 5 and 6 ")
    elif (num%5==0 and num%6!=0):
        print(f"{num} is only divisible by 5")
    elif (num%6==0 and num%5!=0):
        print(f"{num} is only divisible by 6")
    else :
        print("number is niether divisible by 5 nor 6")

divisibility_by_five_six()

#8
def calculate_perimeter():
    s1=int(input("enter length of side 1 triangle : "))
    s2=int(input("enter length of side 2 triangle : "))
    s3=int(input("enter length of side 3 triangle : "))

    if((s1+s2)<s3 or (s2+s3)<s1 or (s1+s3)<s2):
        print("invalid input")
        print("sum of length of two side cannot be lesser than length of third  ")
    else:
        print(f"perimeter of triangle is {s1 + s2 + s3}")


calculate_perimeter()


#9
def hexdecimal_to_decimal():
    deciVal_of_hexChar={"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    keySet_hexChar=list(deciVal_of_hexChar.keys())
    hexChar=input("enter any hex char : ")

    # isaplpha() checks whether all char in a string are alphabet or not
    # isdigit() checks whether all char in a string is a digit between 0-9 or not
    # ord(char) return ascii value of that character 
    # chr(num) return ascii char corresponding to num
    if hexChar.isalpha():
        if hexChar in keySet_hexChar:
            print(f"deciamal value of entered hexadeciamal character is {deciVal_of_hexChar[hexChar]}")
        else:
            print("entered character is not a hexadecimal character")

    elif int(hexChar) in range (0,10):
        print(f"deciamal value of entered hexadeciamal character is {int(hexChar)}") 

    else:
        print("entered character is not a hexadecimal character ")

hexdecimal_to_decimal()