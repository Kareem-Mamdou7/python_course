def calculate_name_score(first_name, second_name):
    first_score, second_score = 0, 0
    true_letters = {"T", "R", "U", "E"}
    love_letters = {"L", "O", "V", "E"}

    both_names = (first_name + second_name).upper()

    for letter in both_names:
        if letter in true_letters:
            first_score += 1

        if letter in love_letters:
            second_score += 1

    print(f"{first_score}{second_score}")


calculate_name_score("Angela Yu", "Jack Bauer")
