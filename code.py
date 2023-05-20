products =  {"Product A": 20,"Product B": 40,"Product C": 50}
def apply_discount(cart):
    sub_total = 0
    shipping_fee = 0
    gift_wrap_total_fee = 0
    total_quantity = 0
    bulk_10_discount = 0
    flat_10_discount = 0
    bulk_5_discount = 0
    tiered_50_discount = 0
    
    for i in range(3):
        total_quantity += cart[i][1]
        sub_total += cart[i][1]*cart[i][2]
        if cart[i][3]==True:
            gift_wrap_total_fee += 1*cart[i][1]
        
    if sub_total > 200:
        flat_10_discount = sub_total - 10
        
    if total_quantity > 20:
        bulk_10_discount = sub_total - sub_total*0.1
        
    for i in range(3):
        if cart[i][1]>10:
            bulk_5_discount += cart[i][1]*cart[i][2]*0.05
    bulk_5_discount = sub_total - bulk_5_discount
    
    if(total_quantity>30):
           for i in range(3):
                if(cart[i][1]>15):
                    tiered_50_discount += (cart[i][1]-15)*cart[i][2]*0.5
    tiered_50_discount = sub_total - tiered_50_discount
    
    total_discount = [flat_10_discount,bulk_5_discount,bulk_10_discount,tiered_50_discount]
    discount_price = min(total_discount)
    index = total_discount.index(discount_price)
    discount_names = ['flat_10_discount','bulk_5_discount','bulk_10_discount','tiered_50_discount']
    total_package = total_quantity//10
    if total_quantity%10 != 0:
        total_package += 1
    shipping_fee = total_package*5
    return(sub_total,discount_names[index],discount_price,shipping_fee,gift_wrap_total_fee)
    
                    
cart=[]
for product, price in products.items():
    quantity = int(input(f"Enter the quantity for {product}: "))
    is_gift_wrap = input(f"Do you want to wrap {product} as a gift? (yes/no): ").lower() == "yes"
    cart.append([product, quantity, price, is_gift_wrap])
    
sub_total,discount_name,discount_price,shipping_fee,gift_wrap_total_fee = apply_discount(cart)

print("Product Name\tQuantity\tTotal")

for product, quantity, price, _ in cart:
    print(f"{product}\t\t{quantity}\t\t{price * quantity}")

print(f"\nSubtotal: ${sub_total}")
if discount_price > 0:
    print(f"Discount Applied: {discount_name}")
    print(f"Discount Price: ${sub_total - discount_price}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_total_fee}")
print(f"Total: ${discount_price+shipping_fee+gift_wrap_total_fee}")    

