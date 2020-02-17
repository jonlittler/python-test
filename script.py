import sys
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello {}".format(who_to_greet)
    return greeting


print(greet("World!"))
print(greet("Jon!"))

r = requests.get("http://www.jonlittler.com")
print(r.status_code)

name = input("Your Name? ")
print("Hello,", name)
