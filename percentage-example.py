# get 10% of 525
# Equation: VALUE X PERCENTAGE / 100 or VALUE X PERCENT_DECIMAL
value = 525
percentage = 10
result = value * percentage / 100
print("%d%% of %d is %d" % (percentage, value, result))

### get the percentage of value from full value
# get % of 15 from 1500
# Equation: VALUE / FULLVALUE X 100
value = 15
fullValue = 1500
result = value / fullValue * 100
print("The %d represents %d%% of %d" % (value, result, fullValue))

### increace percent value
fullValue = 10000
percentage = 3
wrongResult = fullValue * (1 + percentage/ 100) # wrong equation: FULLVALUE * ( 1 + PERCENTAGE / 100)
rightResult = fullValue / ((100 - percentage) / 100) # right equation: FULLVALUE / ( (100 - PERCENTAGE) / 100)
print("The wrong increase of %d%% in the value: %d, is: %f" % (percentage, fullValue, wrongResult))
print("The right increase of %d%% in the value: %d, is: %f" % (percentage, fullValue, rightResult))

### decrease percent value
# remove 3% to value 10000
# equation: FULLVALUE * (1 - PERCENTAGE/100)
wrongDescrease = wrongResult * (1 - percentage/ 100)
rightDescrease = rightResult * (1 - percentage/ 100)

print("The wrong decrease of %d%% in the value: %d, is: %f" % (percentage, wrongResult, wrongDescrease))
print("The right decrease of %d%% in the value: %d, is: %f" % (percentage, rightResult, rightDescrease))