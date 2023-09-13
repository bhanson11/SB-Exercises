def greet(person):
    return f"Hello there, {person}"

def divide(a,b):
    if type(a) is int and type(b) is int:
        return a/b
    return 'a and b must be integers!'

def three_things(a,b,c): 
    print("HII")

def send_email(to_email, from_email, subject, body):
    email = f"""
        to: {to_email}
        from: {from_email}
        subject: {subject}
        -----------------------
        body: {body}
    """
    print(email)

send_email(subject="MEOW", to_email="blue@gmail.com", from_email="colt@humans.com", body="Hi blue, you are my cat. I love you")


def power(num, power=2): #default to squaring or power of 2
    return num ** power 


def add_limited_numbers(a,b):
    """Add two numbers, making sure sum caps at 100."""

    sum = a + b

    # If this required explanatino, comment like this 

    if sum > 100:
        sum = 100

    return sum