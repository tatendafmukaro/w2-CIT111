import math
# The following prompts for two integer values
m_items = int(input("Enter the number of items: "))
p_items = int(input("Enter the number of items per box: "))

# The following lines of code computes the number of boxes needed based 
# the values entered by the user for the manufactured items and number of packed items.
z = (m_items // p_items ) 
#print(math.ceil(z))
boxes_needed = math.ceil(z) + 1

# This print statement outputs the numbers of boxes  needed as per the prompt given.
print (f"For {m_items} items, packing {p_items} items in each box, you will need {boxes_needed} boxes.")

