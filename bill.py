units=int(input("enter the units consumed?:"))
if(units<100):
    amount=units * 3.36
elif(units<=50):
    amount=units * 1.45
elif(units<=150):
    amount=units * 4.30
fixcharge=100
carryingsizecharge=units*1.35
fueladjustmentsize=3.20
total=(amount + fixcharge + carryingsizecharge + fueladjustmentsize)

#Electriciy charges
Electricitycharges= (int(sum*10)/100)
total=amount=(amount+fixedcharge + carryingsizecharge + fueladjustmentsize + Electricitycharges)
round=round(Total)
print("\nElectricity Bill = %.2f" %round)




            
            
            
    




