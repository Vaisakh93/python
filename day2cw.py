
header = """\n\tBOOKSTORE RECEIPT
\t------------------
"""

item1 = "\tBOOK TITLE: {}\t– ₹{}".format("Python Basics", 450)
item2 = "\tBOOK TITLE: {}\t– ₹{}".format("Data Science Intro", 600)

total = 450 + 600
total_line = "\n\tTOTAL AMOUNT:\t₹{}".format(total)

thank_you = "\n\n\tTHANK YOU FOR SHOPPING WITH US!"

receipt = header + item1 + "\n" + item2 + total_line + thank_you

print(receipt.upper())
