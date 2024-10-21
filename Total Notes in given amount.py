amount=int(input("Enter the Total Amount:"))

amount1=amount//2000
amount2= (amount-(amount1*2000))//500
amount3= ((amount-(amount1*2000))-(amount2*500))//100
amount4= ((amount-(amount1*2000))-(amount2*500)-(amount3*100))//50

total_notes= amount1+amount2+amount3
print("Total Notes in the amount are:", total_notes, "\n"
      "2000 Notes: ", amount1, '\n'
      "500 Notes: ", amount2, '\n'
      "100 Notes: ", amount3, '\n'
      "50 Notes: ", amount4)
