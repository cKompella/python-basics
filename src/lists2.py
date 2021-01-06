#list manipulation
toppings = ['pepperoni', 'pineapple', 'cheese','sausage','olives','anchovies','mushrooms']
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
print('We sell '+str(num_pizzas)+' different kinds of pizza!')

pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
print('sorted: ')
print(pizzas)

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#challenge1: appends the size of input list and returns list
def append_size(list):
  list.append(len(list))
  return list

#challenge2: append sum of last two list elements thrice
def append_sum(list):
  for i in range(3):
    list.append(list[-2]+list[-1])
  return list

#challenge3: returns last element of larger list
def larger_list(list1, list2):
  if(len(list1)>=len(list2)):
    return list1[-1]
  return list2[-1]

#challenge4: returns True if item appears in list >n times
def more_than_n(list, item, n):
  if(list.count(item)>n):
    return True
  return False

#challenge5: returns sorted and combined list
def combine_sort(list1, list2):
  list3 = list1+list2
  return sorted(list3)

#challenge6: returns list of every third number between start and 100
def every_three_nums(start):
  return list(range(start, 101, 3)) 

#challenge7: returns list with elements between start and end(inclusive) removed
def remove_middle(list, start, end):
  return list[:start] + list[end+1:]

#challenge8: returns most frequently occuring item in list
def more_frequent_item(list, item1, item2):
  if(list.count(item1)>=list.count(item2)):
    return item1
  return item2

#challenge9: returns new list with element at index doubled
def double_index(list, index):
  if(index>=len(list)):
    return list
  list1 = list 
  list1[index] = list[index]*2
  return list1 

#challenge10: returns middle element of list
def middle_element(list):
  if(len(list)%2==0):
    return (list[int(len(list)/2)] + list[int(len(list)/2)-1])/2
  else:
    return list[int(len(list)/2)]
  
'''
tuples
 - can store different data types
 - immutable, no assignment
 - used to categorize data (one person's info)
'''

