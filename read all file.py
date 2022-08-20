import glob
# All files and directories ending with .txt and that don't begin with a dot:
listing = glob.glob("*")
print(len(listing))
descript = []
for item in listing:
    with open (item, 'rt') as myfile:  # Open lorem.txt for reading
        for i,myline in enumerate(myfile):              # For each line, read to a string,
            if i == 1:
                descript.append(myline)
#print(descript)                  # and print the string.

# open file in write mode
with open(r"C:\Users\User\Downloads\#012963 - BSM - PM Q2\1. EEE.BP (EB.OD.ERROR)/result 1.txt", 'w') as fp:
    for item in descript:
        # write each item on a new line
        fp.write("%s" % item)
    print('Done')