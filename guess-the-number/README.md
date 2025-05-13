if feedback == "h":
high = guess - 1

if our secret number is 6, and computer guess number is 8,
so anything above 8 we are not considering. so we do 'guess - 1'
and assign back to the 'high' to 'guess = random.randint(low, high)'

elif feedback == "l":
low = guess + 1

if our secret number is 6, and computer guess number is 4,
so anything below 4 we are not considering. so we do 'guess + 1'
and assign back to the 'low' to 'guess = random.randint(low, high)'
