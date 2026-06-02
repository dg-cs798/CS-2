""" Lab 1, 3 functins, vote program"""

def vote_menu():
    print("---------------------")
    print("VOTE MENU")
    print("---------------------")
    print("v: Vote")
    print("x: Exit")

    user_option = input("Option: ").strip().lower()

    while user_option != "v" and user_option != "x":
        user_option = input("Invalid (v/x): ").strip().lower()
    return user_option

def candidate_menu():
    print("---------------------")
    print("CANDIDATE MENU")
    print("---------------------")
    print("1: John")
    print("2: Jane")
    candidate = input("Candidate: ").strip()
    while candidate != "1" and candidate != "2":
        candidate = input("Invalid (1/2): ").strip()
    return int(candidate) #returns it as int so that comparability is cleaner instead of using strings

def main():
    john_votes = 0
    jane_votes = 0
    user_option = vote_menu()
    while user_option != "x":
        candidate = candidate_menu()
        if candidate == 1:
            john_votes += 1
            print("Voted John")
        elif candidate == 2:
            jane_votes += 1
            print("Voted Jane")
        user_option = vote_menu()
    total_votes = john_votes + jane_votes
    print("------------------------------")
    print(f"John - {john_votes}, Jane - {jane_votes}, Total - {total_votes}")
    print("-------------------------------")

if __name__ == '__main__':
    main()