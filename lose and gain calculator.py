c_p=int(input("Enter Cost Price:"))
s_p=int(input("Enter Selling Price:"))

gain= s_p-c_p
loss= c_p-s_p

gain_pr= gain/c_p*100
loss_pr= loss/c_p*100

if gain>0:
    print("You made a profit of ",gain, "Percent", gain_pr)
elif gain<0:
    print("You have total loss of ", loss, "Percent", loss_pr)
else:
    print("No Profit or Loss")