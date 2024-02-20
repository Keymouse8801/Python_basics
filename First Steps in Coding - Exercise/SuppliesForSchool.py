pen_packages = int(input())
marker_packages = int(input())
liter_cleaner = int(input())
discount = int(input()) / 100

pen_price = pen_packages * 5.80
marker_price = marker_packages * 7.20
cleaner_price = liter_cleaner * 1.20
total_price = pen_price + marker_price + cleaner_price
discount_price = total_price - (total_price * discount)

print(discount_price)