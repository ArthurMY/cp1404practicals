def main():
    score = get_score()
    score_status = determine_score(score)
    print(score_status)


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


def get_score():
    return float(input("Enter score: "))


main()
