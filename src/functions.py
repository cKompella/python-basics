#basic variables and functions
#constants
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32)* 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

#"getting the force"
def get_force(mass, acceleration):
  return mass*acceleration

def get_energy(mass, c=3*10**8):
  return mass*c**2

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies "+ str(train_force)+ " Newtons of force")
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies "+str(bomb_energy)+ " Joules")

#"doing the work"
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does "+str(train_work)+ " Joules of work over "+str(train_distance)+ " meters.")

#challenges 
def tenth_power(x):
  return x**10

def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return num*3