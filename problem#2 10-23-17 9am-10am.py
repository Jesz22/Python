rainfile = open("rainfall.txt", "r")
outfile = open("rainfallfmt.txt", "w")

for aline in rainfile:
    values = aline.split()
    city = values[0]
    inches = float(values[0])

    outfile.write("%+25s %5.1 f nn" % (city,inches))

rainfile.close()
outfile.close()
