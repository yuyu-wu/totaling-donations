# Totaling Donations Exercise
# Given the provided dictionary of donations:

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0) 

# Use a loop to calculate the total value of the donations.  Save the result to a variable called total_donations 

total_donations = 0

print(donations.values())
for v in donations.values(): 
    print(v)
    total_donations += v
print(total_donations)