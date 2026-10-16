# 1. The first bug I fixed was in the total calculation.
# The code was replacing the total instead of adding each
# sale together. I found it after asking AI to help review
# the code. This showed me that I need more practice finding
# mistakes on my own, especially when using loops.

# 2. The apply_discount function takes two inputs, the
# original price and the customer's discount tier.
# It checks the tier and applies the correct discount.
# Gold gets 15% off, silver gets 10%, bronze gets 5%,
# and any other tier gets no discount. The function
# returns the new price after the discount. A colleague
# could use it as long as they knew the available tiers.

# 3. I used ChatGPT to help review my code, find errors,
# and understand how to fix them. AI helped me understand
# the mistakes by explaining what was wrong and why.
# It also made fixing the code faster, but I still ran
# the program and checked that the output was correct.

# Exercise 1

# Defining a function 
def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2 

def apply_discount(price, tier):
    if tier == 'gold':
        return price * 0.85  # 15% discount
    elif tier == 'silver':
        return price * 0.90  # 10% discount
    elif tier == 'bronze':
        return price * 0.95  # 5% discount
    else:
        return price  # No discount

# Calling the function with different tiers
original_price = 200

for tier in ['gold', 'silver', 'bronze', 'none']:
    print(f"Price for {tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tier ,tax_rate ):
    discounted_price = apply_discount(price,tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 'gold', 0.07): = ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4
orders = [ (200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none') ]
rate = 0.07
for price, tier in orders:
    total = final_price(price, tier, .07)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")

# Exercise 5 
# Bug 1
sales = [120, 80, 250, 175, 90] 
total = 0
for sale in sales: 
    total += sale
print(f"Total: ${total}")
# Bug 2 
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
# Bug 3
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
# Exercise 6
x = 100 # global x
def double_it():
    x = 999 # local x
    return x * 2
print(x)
print(double_it())
print(x)
# The first print shows 100 bc x is a global variable.
#  The function has its own local x with a value of 999. 
# The function returns 1998 bc 999 * 2 = 1998. 
# The last print still shows 100 bc the global x never changed.