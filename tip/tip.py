def main():
    dollars = dollats_to_float(input("how much was the meal? "))
    precent = precent_to_float(input("what precent would you like to tip? "))
    tip = dollars * precent
    print(f"leave ${tip:.2f}")

def dollats_to_float(d):
    return float(d.replace("$", ""))

def precent_to_float(p):
    return float(p.replace("%", "")) / 100

main()