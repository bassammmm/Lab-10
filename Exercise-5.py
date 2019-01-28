def compare_guests(parents_dic,my_dic):
    final_dic = {}

    for key,val in parents_dic.items():
        if key in my_dic.keys():
            final_dic[key] = set(val + my_dic[key])
        else:
            final_dic[key] = val

    for key,val in my_dic.items():
        if key not in final_dic.keys():
            final_dic[key] = val
    num=0
    for key,val in final_dic.items():
        num+=len(val)
    print("\n\nTotal number of families is:",len(final_dic.keys()))
    print("Total number of guests is  :",num)
    print("{:^10}:{:^20}".format("Family","Members"))
    for k,v in final_dic.items():
        print("{:^10}:{:^20}".format(k,str(v)))


parents_dic = {"qazi":["Hussain Qazi","Shabano Qazi","Ali Qazi","Talha Qazi","Rija Qazi"],
               "khan":["Saad Khan","Wajiha Khan","Safi Khan","Arfa Khan"],
               "fawad":["Ali Fawad","Asma Fawad","Usman Fawad","Sumaira Fawad"],
               "hussain":["Mazhar Hussain","Rozina Hussain","Jahanzaib Hussain","Ana Hussain"],
               "mughal":["Nabeel Mughal","Arisha Mughal","Uzair Mughal"]
               }
print("My list")
print("{:^10}:{:^20}".format("Family", "Members"))
for k, v in parents_dic.items():
    print("{:^10}:{:^20}".format(k, str(v)))
my_dic = {"qazi":["Hussain Qazi","Shabano Qazi","Ali Qazi","Talha Qazi","Maham Qazi"],
               "khan":["Saad Khan","Wajiha Khan","Safi Khan","Arfa Khan"],
               "fawad":["Ali Fawad","Asma Fawad","Usman Fawad","Sumaira Fawad"],
               "hussain":["Mazhar Hussain","Rozina Hussain","Jahanzaib Hussain","Ana Hussain"],
          "navivala":["Uzair Navivala","Alisha Navivala","Omair Navivala","Amna Navivala"]}
print("\n\nParents list")
print("{:^10}:{:^20}".format("Family", "Members"))
for k, v in my_dic.items():
    print("{:^10}:{:^20}".format(k, str(v)))
compare_guests(parents_dic,my_dic)