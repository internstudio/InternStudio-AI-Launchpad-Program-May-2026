# Electricity Bill Calculator
# This script calculates the electricity bill based on tiered rates and applies GST and warnings.

def calculate_bill(units):
    # Rates per unit
    rate1 = 5   # first 100 units
    rate2 = 7   # next 100 units (101-200)
    rate3 = 10  # above 200 units
    bill = 0
    if units <= 100:
        bill = units * rate1
    elif units <= 200:
        bill = 100 * rate1 + (units - 100) * rate2
    else:
        bill = 100 * rate1 + 100 * rate2 + (units - 200) * rate3
    return bill

def apply_gst(bill_amount):
    # Apply 18% GST if bill exceeds ₹2000
    if bill_amount > 2000:
        return bill_amount * 1.18
    return bill_amount

def main():
    name = input("Enter customer name: ")
    while True:
        try:
            units = float(input("Enter units consumed: "))
            if units < 0:
                print("Units cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for units.")
    base_bill = calculate_bill(units)
    total_bill = apply_gst(base_bill)
    print(f"\n--- Electricity Bill for {name} ---")
    print(f"Units Consumed : {units}")
    print(f"Base Amount    : ₹{base_bill:.2f}")
    if base_bill != total_bill:
        print(f"GST (18%)      : ₹{total_bill - base_bill:.2f}")
    print(f"Total Amount   : ₹{total_bill:.2f}")
    if units > 300:
        print("Warning: High Power Consumption")

if __name__ == "__main__":
    main()
