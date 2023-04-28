#1
def miles_to_kilometer():
    from prettytable import PrettyTable
    myTable= PrettyTable(["miles", "kilometers"])

    for i in range(1,11):
        myTable.add_row([i,1.609*i])

    print(myTable)

miles_to_kilometer()

#2
def calc_tutionFee():
    
    def tut_fee_after_n_year(no_of_year, initial_fee):
        
        for i in range(0, no_of_year):
            initial_fee*=1.05
        
        nth_year_fee=initial_fee
        return nth_year_fee
    
    current_fee=10000

    def fee_in_a_period(initial_year, final_year): # consider current year to be 0

        total_fee=0

        for i in range(initial_year, final_year+1):
            total_fee+=tut_fee_after_n_year(i,current_fee)
        
        return total_fee
    
    print("tution fee of 4 year after 10 year from now",fee_in_a_period(10,13))

calc_tutionFee()



#3
def number_divisible_by_5and6():
    ten_num_list=[]

    def is_divisible_5and6(n):
        if(n%5==0 and n%6==0):
            return True
        else:
            return False
    
    for num in range(100, 1000+1):
        
        if len(ten_num_list)==10 or num==1000:
            print(ten_num_list)
            ten_num_list.clear()

        if is_divisible_5and6(num):
            ten_num_list.append(num)

number_divisible_by_5and6()

#4
def ascii_chars():
    from prettytable import PrettyTable
    my_table =PrettyTable(["1","2","3","4","5","6","7","8","9","10"])
    count=33
    print("\ntable of ascii character fron ! to ~\n")

    while count<=127:
        my_table.add_row([chr(count),chr(count+1),chr(count+2),chr(count+3),chr(count+4),chr(count+5),chr(count+6),chr(count+7),chr(count+8),chr(count+9)])
        count+=10
    
    print(my_table)


ascii_chars()

#5
def number_triangles():
    for i in range(1,6+1):
        for j in range(1,6+1):
            if(j<=i):
                print(j,end=" ")
        print("")

    print("\n")
    for i in range(1,6+1):
        for j in range(1,6+1):
            if(j-i>=0):
                print(j-i+1,end=" ")
        print("")

    print("\n")
    for i in range(1,6+1):
        for j in range(1,6+1):
            if(j+i<7):
                print(" ",end=" ")
            else:
                print(7-j,end=" ")
        print("")

    print("\n")
    for i in range(1,6+1):
        for j in range(1,6+1):
            if(j-i>=0):
                print(j-i+1,end=" ")
        print("")

number_triangles()

#6
def number_pyramid():
     
    n_rows=6
    n_cols=2*n_rows-1
    
    row=1
    num=1


    while (row<=n_rows):
        col=1
        while(col<n_cols):
            if(col<= n_rows-row):
                print(" ", end="  ")
                
                col+=1
            elif(col> n_rows-row and col<n_rows):
                print(int(num), end="  ")
                num*=2
                col+=1
            elif(col==n_rows):
                print(int(num),end="  ")
                col+=1
            elif(col>n_rows and col< n_rows+row):
                num/=2
                print(int(num), end="  ")
                col+=1
                
            else:
                col+=1
        row+=1
        print("")
    
number_pyramid()

#7
def calc_payable_amount():
    from prettytable import PrettyTable 
    loan_amount=int(input("enter the loan amount : "))
    n_year= int(input("enter load period in years : "))
    interest_rate=5
    total_payment=loan_amount+ loan_amount*interest_rate*n_year


    my_table=PrettyTable(["intrest", "total payable amount "])

    while (interest_rate<=8):
        total_payment=loan_amount+ loan_amount*interest_rate*n_year
        my_table.add_row([interest_rate, total_payment ])
        interest_rate+=1/8

    print(my_table)

calc_payable_amount()

#8
def loan_schedule():
    monthly_interest_rate= 0.01
    n_year=4
    loan_amount=1000000
    balance = loan_amount 

    monthly_payement= (loan_amount + loan_amount*monthly_interest_rate*12*n_year)/(12*n_year)
    print("monthly payement : " , monthly_payement)

    print("I", "\t\t", "INTEREST", "\t", "PRINCIPAL", "\t", "BALANCE")
    for i in range(1, n_year*12 +1):
        interest=monthly_interest_rate*balance
        principal=monthly_payement-interest
        balance=balance-principal
        if(balance>=principal):
            print(i, "\t\t", int(interest), "\t\t", int(principal), "\t\t", int(balance))
        else:
            print(i, "\t\t", int(interest), "\t\t", int(balance), "\t\t", int(balance))
            balance=0
            break

loan_schedule()

#9
def perfect_nums_in_range(max_limit):
    def is_perfect_number(num):
        divisor_list=[]
        for i in range(1,num//2+1):
            if(num%i==0):
                divisor_list.append(i)
                divisor_list.append(num//i)
        
        divisor_set=set(divisor_list) # (| for union ), (& for intersection ), (- for setA minus setB) , (^ for union minus intersection )
        unique_divisors=list(divisor_set)

        from functools import reduce
        sum_of_divisor= reduce(lambda x,y:x+y, unique_divisors) - num
        # print("sum of all divisor : ", sum_of_divisor)
        if sum_of_divisor==num:
            return True
        else:
            return False     


    for i in range(2, max_limit +1):
        if (is_perfect_number(i)):
            print(i," is perfect number")

perfect_nums_in_range(10000)

#10
def all_combination_in_range(range_lower_bound,range_upper_bound):
    class combination:
        '''for storing pair of two num'''
        def __init__(self,n1,n2):
            self.n1=n1
            self.n2=n2

        # def __str__(self):
        #     return "({0},{1})".format(self.n1, self.n2)

        def __repr__(self):
            return "({0},{1})".format(self.n1, self.n2)
        
        def __eq__(self, other):
            return (self.n1 == other.n1 and self.n2 == other.n2) or (self.n1 == other.n2 and self.n2 == other.n1)

        def __hash__(self):
            return hash(frozenset((self.n1, self.n2))) # frozenset  is an immutable set in python 

    # range_lower_bound=1
    # range_upper_bound=7

    range_list=[i for i in range(range_lower_bound,range_upper_bound+1)]

    print(range_list)

    combination_set=set()

    for i in range_list:
        for j in range_list:
            if(i!=j):
                pair= combination(i,j)
                combination_set.add( pair)

    print("total possible combination are : ", len(combination_set))
    # print(combination_set)
    i=1
    for pair in combination_set:
        print(i,". ", pair)
        i+=1

all_combination_in_range(1,7)











