class MymultipleFunctions():
    def Subfields():
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in list:
            print(i)
    def OddEven():
        t=(int(input("Enter the Number: ")))
        if(t%2 == 0):
             print(t, " is Even number")
             out="Even Number"
             return out
        else:
             print(t, " is Odd number")
             out="Odd Number"
             return out
    def percentage():
        S1=int(input("Subject1 :"))
        S2=int(input("Subject2 :"))
        S3=int(input("Subject3 :"))
        S4=int(input("Subject4 :"))
        S5=int(input("Subject5 :"))
        total = S1 + S2 + S3 + S4 + S5
        per = (total / 500.0) * 100;
        print("Subject1 :",S1)
        print("Subject2 :",S2)
        print("Subject3 :",S3)
        print("Subject4 :",S4)
        print("Subject5 :",S5)
        print("Total :",total)
        print("Percentage :",per)
    def Elegible():
        gen=input("Enter your Gender(Male or Female):").strip().lower()
        a=int(input("Enter your Age :"))
        if (a >= 21 and gen == "male"):
            res="Elegible"
            print("Your Gender: ",gen)
            print("Your Age: ",a)
            print("Elegible")
            return res
        elif (a >= 18 and gen == "female"):
            res="Elegible"
            print("Your Gender: ",gen)
            print("Your Age: ",a)
            print("Elegible")
            return "Elegible"
        else:
            res="Not Elegible"
            print("Your Gender: ",gen)
            print("Your Age: ",a)
            print("Not Elegible")
            return res
    def triangle():
        H=int(input("Height: "))
        B=int(input("Breadth: "))
        #print("Area of Triangle")
        print("Area formula: (Height*Breadth)/2")
        aot=(H*B)/2
        print("Area of Triangle:  ", aot)
        #print("Perimeter of Triangle")
        H1=int(input("Height1: "))
        H2=int(input("Height2: "))
        B2=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth ")
        pot=H1+H2+B2
        print("Perimeter of Triangle: ", pot)


