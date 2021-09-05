"""
CP1404/CP5632 Practical - Suggested Solution
State names in a dictionary
File has been reformatted and state inputs can be any case
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

for state, state_key in CODE_TO_NAME.items():
    print("{:3} is {}".format(state, state_key))