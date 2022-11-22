import random
MENU = """(G)et a valid score
(P)rint result 
(S)how stars
(Q)uit"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = random.randrange(0, 100)
            print(score)
        elif choice == "P":
            score_status = determine_score(score)
            print(score_status)
        elif choice == "S":
            print(f"{score * '*'}")
        else:
            print("invalid input")
        print(MENU)
        choice = input(">>>").upper()
    print("END.")


def determine_score(score):
    if score < 0:
        score_status = "Invalid score"
    else:
        if score > 100:
            score_status = "Invalid score"
        elif score >= 90:
            score_status = "Excellent"
        elif score >= 50:
            score_status = "Passable"
        else:
            score_status = "Bad"

    return score_status


main()
