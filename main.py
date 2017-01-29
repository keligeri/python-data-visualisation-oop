from controller import Controller


def main():
    """Call the methods from Controller class"""

    input_num = 1
    controller = Controller()

    while input_num != "0":
        controller.print_the_menu()
        input_num = input("Choose a number: ")

        if input_num == "1":
            controller.company_by_color()
        elif input_num == "2":
            controller.project_name_by_budget()
        elif input_num == "3":
            controller.bigger_than_average()
        elif input_num == "4":
            controller.name_and_status()

        elif input_num == '0':
            break
        else:
            continue

if __name__ == "__main__":
    main()
