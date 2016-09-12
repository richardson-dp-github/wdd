acceptable_values = []

# Set what are acceptable values for the row count
#  This has to be coordinated with the writer
for i in range(0,10000,100):
    if not i==0:
        acceptable_values.append(i)

verbose = False

acceptable_vals_dict = {}
acceptable_vals_dict[1] = 10
acceptable_vals_dict[2] = 20
acceptable_vals_dict[3] = 30
acceptable_vals_dict[4] = 40
acceptable_vals_dict[5] = 50
acceptable_vals_dict[6] = 60
