def calculateEletronicsGST(a,b):
    add =a+b
    gst = add*18/100
    return add +gst

def calculateFashionGST(c,d):
    fashion = c+d
    GST = fashion*13/100
    return fashion + GST

def calculateFoodGST(e):
    foodgst =e*7/100
    return e + foodgst

def totalBill(a,b,c,d,e):
    electronic =calculateEletronicsGST(a,b)
    fashion = calculateFashionGST(c,d)
    food =calculateFoodGST(e)
    return electronic + fashion + food

def calculateDiscountBill(a,b,c,d,e):
    total = totalBill(a,b,c,d,e)
    discount = total *20/100
    final_amount = total -discount

    return final_amount

a=100
b=100
c=100
d=100
e=100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountBill(a, b, c, d, e)

print(f"Electronics: {calculateEletronicsGST(a, b):.2f}")
print(f"Fashion: {calculateFashionGST(c, d):.2f}")
print(f"Food: {calculateFoodGST(e):.2f}")
print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")
