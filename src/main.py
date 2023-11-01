from gui import run_gui

def main():
    while True:
        run_gui()
        user_input = input("Do you want to perform another operation? (y/n): ")
        if user_input.lower() != 'y':
            break


if __name__ == "__main__":
    run_gui()
    main()