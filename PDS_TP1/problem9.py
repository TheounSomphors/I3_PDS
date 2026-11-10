#(a)
def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)                   
    tier2 = min(max(kwh - 50, 0), 150)      
    tier3 = max(kwh - 200, 0)              

    subtotal = tier1 * 480 + tier2 * 610 + tier3 * 730
    total = (subtotal + 2000) * 1.10        # add fee, then 10% VAT
    return round(total)


# (b) Table
RATE = 4100
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / RATE
    print(f"{kwh:>3} kWh -> {bill:>10,} riel (≈ {usd:>6.2f} USD)")


# (c) User input
kwh = float(input("Enter your monthly consumption (kWh): "))
bill = electricity_bill(kwh)
if bill is None:
    print("Invalid input: consumption cannot be negative.")
else:
    print(f"Your bill: {bill:,} riel (≈ {bill / RATE:.2f} USD)")