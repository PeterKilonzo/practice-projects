def analyze_profits(revenue, costs):
    profit = revenue - costs
    net_profit = profit - 250
    return profit, net_profit

revenue1 = int(input("enter revenue for first quarter:"))
cost1 = int(input("enter cost for first quarter:"))
first_quarter = analyze_profits(revenue1, cost1)

print("the gross profit for the first quarter is", first_quarter[0])
print("the net profit for the first quarter is",first_quarter[1])


revenue2 = int(input("enter revenue for second quarter:"))
cost2 = int(input("enter cost for second quarter:"))
second_quarter = analyze_profits(revenue2, cost2)

print("the gross profit for the second quarter is", second_quarter[0])
print("the net profit for the second quarter is", second_quarter[1])

if second_quarter[0] > first_quarter[0]:
    print('reward the team')

else:
    print('we need a new CEO!')
