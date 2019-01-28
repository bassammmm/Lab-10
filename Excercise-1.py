my_family = {
    "Father":"Mehshar Hussain",
    "Mother":"Shabana Mehshar",
    "Siblings":["Eshaal"]
}
for k,v in my_family.items():
    print("{:^10}:{:^20}".format(k,str(v)))

grand_family = {
    "Maternal":{"Grand Father":"Zulqarnain Haider",
                "Grand Mother":"Shumaila Haider",
                "Uncles":["Usman Haider","Ali Haider"],
                "Aunts":["Farhana Haider","Farzana Haider"]
                },
    "Paternal":{"Grand Father":"Muzaffar Hussain",
                "Grand Mother":"Hafeeza Begum",
                "Uncles":["Mufassir Hussain","Mubashir Hussain"],
                "Aunts":["Asma Hussain","Afshan Hussain"]
                }
}
my_family.update(grand_family)
print("\nAfter update :-\n")
for k,v in my_family.items():
    if isinstance(v,dict):
        print("{:^20}:-".format(k))
        for key,val in v.items():
            print("{:^20}:{:^20}".format(key,str(val)))
    else:
        print("{:^20}:{:^20}".format(k,str(v)))