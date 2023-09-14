print("""
""")
weight = int(input("Enter your weight:- "))
unit = input("""
            Enter the required:- 
            ------------------
                (K) gs or (L) bs:- """).upper()

if unit == "K":
    converted1 = weight * .45
    print("""
    """)
    print(f"Your weight in (K) gs is {converted1}")
else:
    converted2 = weight / .45
    print("""
    """)
    print(f"Your weight in (L) bs is {converted2}")
