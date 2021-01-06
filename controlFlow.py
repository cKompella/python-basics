#asks users for package weight, determines best shipping method and its cost

#finds ground_shipping_cost
def ground_shipping_cost(weight):
  return weight*4.0+20
#finds drone_shipping_cost
def drone_shipping_cost(weight):
  return weight*4.5
#finds cheapest shipping method
def cheapest_shipping(weight):
  drone_cost = drone_shipping_cost(weight)
  ground_cost = ground_shipping_cost(weight)
  if(drone_cost<ground_cost and drone_cost<premium_ground_shipping_cost):
    return "Drone shipping is cheapest: "+str(drone_cost)
  elif(ground_cost<premium_ground_shipping_cost and ground_cost<drone_cost):
    return "Ground shipping is cheapest: "+str(ground_cost) 
  else:
    return "Premium shipping is cheapest: "+str(premium_ground_shipping_cost)

#testing
print(cheapest_shipping(4.8))
print(cheapest_shipping(50))


