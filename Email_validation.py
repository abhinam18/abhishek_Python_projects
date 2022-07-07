email= input("Enter the Email: ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@ in email") and (email .count("@")==1):
            if email[-4] in ".edu, .com, .in, .gov, .edu":
                for i in email:
                    if i== i.isspace():
                       k=1
                    elif i.isalpha():
                        if i==i.isupper():
                            j==1
                    elif i.isdigit():
                        continue
                    elif i== "_" or i=="@" or i==".":
                        continue
                    else:
                        d=1
                    if (k==1) or (j==1) or (d==1):
                        print("wrong email-6")
                if k==1:
                   print("Invaild email-5")
                print("Vaild email")
            else:
                print("wrong email id-4")
        else:
            print ("wrong email id-3")
    else:
        print ("wrong email id-2 ")
else:
    print ("wrong email id-1")