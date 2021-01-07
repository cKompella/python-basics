#for loops, while loops, list comprehension
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
average_price = 0
total_revenue = 0
#calculates total price
for price in prices:
  total_price+=price
average_price = total_price/len(prices)
print("Average Haircut Price: $"+str(average_price))

#populates new_prices with 5 less than prices[i]
new_prices = [price-5 for price in prices]
print(new_prices)

#calculates total_revenue
for i in range(len(hairstyles)):
  total_revenue+= prices[i]*last_week[i]
print("Total Revenue: $"+str(total_revenue))
average_daily_revenue = total_revenue/7
print("Average daily revenue: $"+str(average_daily_revenue))

#populates cuts_under_30 with hairstyles costing less than 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i]<30]
print(cuts_under_30)


#challenge1: returns number of elements divisible by 10
def divisible_by_ten(nums):
  num=0
  for i in nums:
    if(i%10==0):
      num+=1
  return num

#challenge2: returns new list with "Hello," concatenated to each names element
def add_greetings(names):
  list = ["Hello, "+name for name in names]
  return list

#challenge3: removes elements from front of lst until front of the list is odd
def delete_starting_evens(lst):
  while lst[0]%2==0:
    if(len(lst)==1):
      return []
    lst = lst[1:]
  return lst

#challenge4: returns list with every odd-indexed lst element
def odd_indices(lst):
  odds = []
  #way1
  # index = 0
  # while(index<len(lst)):
  #   if(index%2==0):
  #     index+=1
  #     continue
  #   odds.append(lst[index])
  #   index+=1
    #way2
  odds = [lst[i] for i in range(len(lst)) if i%2==1]
  return odds

  #challenge5: retuns list with every bases element raised to every powers element
  def exponents(bases, powers):
  index=0
  result = []
  for i in range(len(bases)):
    for j in range(len(powers)):
      result.append(bases[i]**powers[j])
  return result

  #challenge6: return list with larger sum
  def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in lst1:
    sum1+=i
  for j in lst2:
    sum2+=j
  if(sum1>=sum2):
    return lst1
  else:
    return lst2

#challenge7: returns sum of lst elements until sum>9000, otherwise sums all lst elements
def over_nine_thousand(lst):
  sum = 0
  for num in lst: 
    sum+=num
    if(sum>9000):
     break
  return sum

#challenge8: returns largest number in nums
def max_num(nums):
  max = nums[0]
  for num in nums:
    if (num > max):
        max = num
        print(num)
  return max

#challenge9: returns list of indices where lst1[i]==lst2[i]
def same_values(lst1, lst2):
  indices = []
  for i in range(len(lst1)):
    if(lst1[i]==lst2[i]):
      indices.append(i)
  return indices
  S
#challenge10: returns True if lst1 equals lst2 reversed
def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if(lst1[i]!=lst2[len(lst2)-i-1]):
      return False
  return True





