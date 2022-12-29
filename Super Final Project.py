def year(p,q):
    a=int(p[-4:])
    b=int(q[-4:])
    x=[]
    y=[]
    for i in range(a,b+1):
        if i%100!=0 and i%4==0:
            x.append(i)
        elif i%400==0:
            x.append(i)
        else:
            y.append(i)
    print("Leap years in range are:",x)
    print("Non-Leap years in range are:",y)


p=input("Enter the date in dd/mm/yyyy format ")
q=input("Enter the range of date in dd/mm/yyyy format ")
if len(p)==len(q):
    if len(p)==10 and len(q)==10:
        m = int(p[3:5])
        n = int(q[3:5])
        c = int(p[0:2])
        d = int(q[0:2])
        e = int(p[6:])
        f = int(q[6:])
        list1 = [1, 3, 5, 7, 8, 10, 12]
        list2 = [4, 6, 9, 11]
        list3 = [2]
        if m <= 12 and n <= 12 and m>0 and n>0 and c>0 and d>0 and e>0 and f>0:
            if e<f:
                if m in list1 and n in list1:
                    if c <= 31 and d <= 31:
                        year(p, q)
                    else:
                        print("Enter valid dates")
                elif m in list1 and n in list2:
                    if c <= 31 and d <= 30:
                        year(p, q)
                    else:
                        print("Enter valid dates")
                elif m in list2 and n in list1:
                    if c<=30 and d<=31:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list2 and n in list2:
                    if c<=30 and d<=30:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list3 and n in list1:
                    if c<=29 and d<=31:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list3 and n in list2:
                    if c<=29 and d<=30:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list1 and n in list3:
                    if c<=31 and d<=29:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list2 and n in list3:
                    if c<=30 and d<=29:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list2 and n in list2:
                    if c<=30 and d<=30:
                        year(p,q)
                    else:
                        print("Enter valid dates")
                elif m in list3 and n in list3:
                    if c<=29 and d<=29:
                        year(p,q)
                    else:
                        print("Enter valid dates")
            else:
                print("First year should be less than the second")
        else:
            print("Enter valid month number")
    else:
        print("Sorry, Inputs are not in DD/MM/YYYY format")
else:
    print("Sorry, Inputs are not in DD/MM/YYYY format")







