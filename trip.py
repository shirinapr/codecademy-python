def hotel_cost(nights):
  # Hotel costs 140$ per nights
  return 140*nights

def plane_ride_cost(city):
  # There are 4 available citites for travel;
  # Charlotte, Tampa, Pittsburgh and Los Angeles.
  if city=="Charlotte":
    return 183
  elif city=="Tampa":
    return 220
  elif city=="Pittsburgh":
    return 222
  else:
    return 475

def rental_car_cost(days):
  # Car rental per day is 40$, if you rent for more than 3 days you get 20$ off,
  # if you rent for more than 40 days you get 50$ off!
  cost=days*40
  if days >= 7:
    cost-=50
  elif days >=3:
    cost-=20
  return cost

def trip_cost(city, days, spending_money):
  # We mesure the trip cost by summing the car rental, hotel, plane_ride and other costs.
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
  