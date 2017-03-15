def robodia(emp):
    count = 0
    for i in emp:
        if i == "shikha" or i =="Anjali" or i == "shuryansh" or i == "sandeep":
              count +=1
        else :
             i = i
     return count
list_robodia = robodia(emp)
print("Number of emp:" + str(robodia(emp))) 
