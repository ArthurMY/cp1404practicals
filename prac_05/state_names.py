CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
state_lists = []
print(CODE_TO_NAME)
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code:<3} is {CODE_TO_NAME[state_code]}")
        state_lists.append(state_code)
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


for i in state_lists:
    print(f"{i:<3}", "is", CODE_TO_NAME[i])
# for state_code, CODE_TO_NAME[state_code] in CODE_TO_NAME[state_code]:
#     print(f"{state_code:<3} is {CODE_TO_NAME[state_code]}")
