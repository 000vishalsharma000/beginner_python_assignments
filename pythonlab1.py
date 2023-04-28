import math

# sum of all number that occur before N
def sum_of_primes(N):
    primes = [2]
    sum_primes = 2
    for i in range(3, N):
        if is_prime(i):
            primes.append(i)
            sum_primes += i
    print(sum_primes) 

def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

# Example usage
sum_of_primes(10) # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19=77

##eucledian distance between two points
def calc_edistance():
    x1= int(input("enter x coordinate of first point")) 
    y1= int(input("enter y coordinate of first point")) 
    x2= int(input("enter x coordinate of second point")) 
    y2= int(input("enter x coordinate of second point")) 

    dist= math.sqrt((x1-x2)**2 + (y1-y2)**2)

    print(dist)


calc_edistance()


#energy in joule 
def calc_energy(water_quantity, i_temp, f_temp):
    energy=water_quantity*(f_temp - i_temp)*4182
    print(f"total energy for water quantity={water_quantity} and intitial temp({i_temp}),final temp({f_temp}) =  {energy}")


calc_energy(1,0,100)


# celcius to fahrenhiet

def convert_temp(c_temp):
    print(f"{c_temp}celcius ={((c_temp*9)/5 +32)} fahrenhiet")


convert_temp(55)


#area , volume of cylinder
def calc_area_vol(r,l):
    area=(44/7)*(r**2) + 44/7*r*l
    volume = (22/7)*(r**2)*l
    print(f"area = {area} and volume = {volume}")


calc_area_vol(7,1)

# convert feets to meter
def convert_feet_meter(feet):
     print(f'{feet} feet in meter are={feet*0.3048}')


convert_feet_meter(10)


#convert pounds to kilo gram
def pound_to_kilo(pound):
    print(f"{pound} pounds in kilograms= {pound/2.2046}")


pound_to_kilo(20)


