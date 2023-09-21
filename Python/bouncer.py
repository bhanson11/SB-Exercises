age = 19
is_birthday = False

if age >= 21:
    print("YOU CAN DRINK.")
    if is_birthday:
        print("HAPPY BIRTHDAY, HERE IS A FREE MARTINI!")
elif age >= 18:
    print("YOU CAN COME IN BUT NO DRINKING!")
    if is_birthday:
        print("HAPPY BIRTHDAY, HERE IS A FREE APPLE JUICE!")
else:
    print("SORRY GO HOME KID!")


# javascript --> do_if_true if CONDITION else do_if_false

# python --> condition ? do_if_true : do_if_false