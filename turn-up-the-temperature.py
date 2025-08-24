def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp


def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


def get_force(mass, acceleration):
    force = mass * acceleration
    return force


def get_energy(mass, c=3 * 10 ** 8):
    energy = mass * c ** 2
    return energy


def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work


# Test farenheit to celcius function, f_to_c
f100_in_celcius = f_to_c(100)
print("100 degrees f in celcius is : " + str(f100_in_celcius))

# Test celsius to farenheit function, c_to_f
c0_in_fahrenheit = c_to_f(0)
print("0 degress celsius in farenheit is: " + str(c0_in_fahrenheit))

# Test variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Test get_force
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Test get_envergy
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")


