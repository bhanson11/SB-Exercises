def get_days_alive(person):
    try:
        days = person['age'] * 365
        print(f'{person["name"]} has been alive for {days} days')
    except KeyError as exc:
        print(f"Missing key: {exc}")
    except TypeError:
        print("Expected person to be a dict")

# LBYL - look before you leap -- more javascript
# EAFP - easier to ask for forgiveness rather than permission