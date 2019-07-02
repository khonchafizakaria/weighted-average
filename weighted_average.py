# How to calculate the weighted average based on a 5 start rating,
# we will use "Decimal" to avoid rounding issues
from decimal import Decimal

# Users
mark_5 = 6234 # Users who have given you 5 stars
mark_4 = 4363 # Users who have given you 4 stars
mark_3 = 3534 # Users who have given you 3 stars
mark_2 = 5654 # Users who have given you 2 stars
mark_1 = 9342 # Users who have given you 1 star

# We will create a dictionnary to ease the iteration
d = {
	"5": mark_5,
	"4": mark_4,
	"3": mark_3,
	"2": mark_2,
	"1": mark_1,
}

total_users = sum([mark_1, mark_2, mark_3, mark_4, mark_5])

# We will use this function to get the share of each group
def mark_percent(group):
	group_share = "{:.1f}".format((group/total_users)*100)
	return group_share

def weighted_average():
	
	# The logic behind the weighted average is, multiply the users of each group by their weight (scale or mark).
	weighted_mark5 = mark_5 * 5 
	weighted_mark4 = mark_4 * 4
	weighted_mark3 = mark_3 * 3
	weighted_mark2 = mark_2 * 2
	weighted_mark1 = mark_1 * 1 

	# sum() everything together.
	total_marks = sum([weighted_mark5, weighted_mark4, weighted_mark3, weighted_mark2, weighted_mark1])

	try:
		avg = Decimal(total_marks/total_users)
		average = "{:.1f}".format(avg)

	# You do not need to set this exception block,
	# In case you are implementing the weighted average in your website, you'll have to set it.
	except ZeroDivisionError:
		average = Decimal(0.0)
	return Decimal(average)

for k,v in d.items():
	print("{}% of your users have given this product a rating of {}".format(mark_percent(v), k))

print("Prdouct was rated {}/5.0".format(weighted_average()))

### OUTPUT ###
# 21.4% of your users have given this product a rating of 5
# 15.0% of your users have given this product a rating of 4
# 12.1% of your users have given this product a rating of 3
# 19.4% of your users have given this product a rating of 2
# 32.1% of your users have given this product a rating of 1
# Prdouct was rated 2.7/5.0


