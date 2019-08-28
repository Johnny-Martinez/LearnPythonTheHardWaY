cars = 100
# floating point variable for space in cars
space_in_car = 4.0
# number of drivers available
drivers = 30
# number of passengers available
passangers = 90
# remaining number of cars after all seats have been taken
cars_not_driven = cars - drivers
# amount of cars driven is equal to drivers on the road
cars_driven = drivers
# number of drivers times amount of space in vehicle.
carpool_capacity = drivers * space_in_car
# average number of seats taken per vehicle on the road.
average_passenger_per_car = passangers / cars_driven

print('There are ', cars, ' cars available.')
print('There are only ', drivers, ' drivers available')
print('There will be ', cars_not_driven, ' empty cars today.')
print('We can transport ', carpool_capacity, ' people today.')
print('We have ', passangers, ' to carpool today.')
print('We need to put about ', average_passenger_per_car, ' in each car.')
