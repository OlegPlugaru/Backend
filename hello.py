# On example of function
moms = [
    ("Ned", "Eleanor"),
    ("Max", "Susan"),
    ("Susan", "Shelly"),
]

def find_mom(moms,child):
    """Find the mom of child."""
    for child_name, mom_name in moms:
        if child == child_name:
            return mom_name
    return None

print(find_mom(moms, "Max"))





# def how_many_grandmothers(moms):
#     """How many moms are grand - moms?"""
#     grandmothers = 0
#     for child, mom in moms:
#         print(child, mom)
#         grandma = find_mom(moms, mom)
#         print(grandma) 
#         if grandma:
#             grandmothers += 1
#     return grandmothers
        

# print(how_many_grandmothers(moms))