def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183 
    elif city == "Tampa":
        return 220 
    elif city == "Pittsburgh": 
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost 

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

def amount_under_budget(spent, tripBudget):
    underAmount = tripBudget - spent
    print ("You were under budget by $" + str(underAmount) + ".")
    return underAmount
    
def amount_over_budget(spent, tripBudget):
    overAmount = spent - tripBudget
    print ("You were over budget by $" + str(overAmount) + ".")
    return overAmount

def budget_proximity(spent, tripBudget):
    if spent < tripBudget:
        return (amount_under_budget(spent, tripBudget))
    elif spent > tripBudget:
        return(amount_over_budget(spent, tripBudget))
    else:
        print ("You have used your exact budget.")
        return 0

# You were planning on taking a trip to LA
# for five days with $600 of spending money.
tripBudget = trip_cost("Los Angeles", 5, 600)
tripCost = budget_proximity(2734, tripBudget)
print (round(tripCost))
