from getpass import getpass

def main():
    user1input = getpass("Welcome to Hangman!\nUser 1, please enter keyword: ")
    num_underscore = user1input.len()
    
    for i in num_underscore:
        print(" _ ")


if __name__ == "__main__":
    main()
