# Easy 2 – Toy Example Using Python Basics

def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"\nHello {name}!")
    print(f"In 5 years, you will be {age + 5} years old.")

    if age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

if __name__ == "__main__":
    greet()
