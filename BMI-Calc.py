# Written by Jack Foster - Last edit 2/4/23
# BMI Calculator
print(("="*8) + " Body Mass Index Calculator " + ("="*8) + "\n ")

# Gather user input for name, height, and weight
Name = input("Please enter your name:")
print("Welcome, " + Name + "!\n")
lbs = float(input("Enter your weight in pounds:"))
feet = float(input("Enter your height (feet):"))
inches = float(input("Enter your height (inches):"))
print("\n" + ("="*15) + " Calculations " + ("="*15))

# Establish variables to convert between imperial and metric units
CONVERT_TO_KILO = 0.45359237
CONVERT_TO_METERS = 0.0254
CONVERT_TO_POUNDS = 2.2046226
LOWBMI = 18.5
HIGHBMI = 24.9

# Converting units and finding BMI given height and weight
TOTAL_INCHES = (feet * 12) + inches
BMI = ((lbs * 703) / (TOTAL_INCHES ** 2))
KILOGRAMS = lbs * CONVERT_TO_KILO
METERS = TOTAL_INCHES * CONVERT_TO_METERS
MetricBMI = (KILOGRAMS / (METERS ** 2))

print("Your BMI using english measurements is " + str(round(BMI, 2)))
print("Your BMI using metric measurements is " + str(round(MetricBMI, 2)) + "\n")

# Calculate healthy weight range based on low BMI of 18.5 and high BMI of 24.9
MetricLowWeight = LOWBMI * (METERS ** 2)
MetricHighWeight = HIGHBMI * (METERS ** 2)

# Convert to pounds
LowWeight = ((LOWBMI * (METERS ** 2)) * CONVERT_TO_POUNDS)
HighWeight = ((HIGHBMI * (METERS ** 2)) * CONVERT_TO_POUNDS)

# Print healthy weight range in pounds and kilograms
print("For your height of " + str(round(TOTAL_INCHES, 1)) + " inches a healthy weight range is between " + str(round(LowWeight, 2)) + " and " + str(round(HighWeight, 2)) + " pounds")
print("For your height of " + str(round(METERS, 2)) + " meters a healthy weight range is between " + str(round(MetricLowWeight, 2)) + " and " + str(round(MetricHighWeight, 2)) + " kilograms")





