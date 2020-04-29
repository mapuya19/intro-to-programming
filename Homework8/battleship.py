"""
A simplified one player version of Battleship. In this version of
Battleship, the computer hides a ship in a 5 x 5 grid.  The player must find
the ship by inputting row and column pairs.  If the player finds the ship,
the player wins. The player has unlimited turns! Additionally, the player
can save or load their progress to a file (though looking at the file will
reveal the location of the ship).
"""

import random


def load_from_file(name_of_file):
    final_list = []

    load_file = open(name_of_file, "r")
    all_data = load_file.read()
    load_file.close()

    loaded_list = all_data.split("\n")
    for i in loaded_list:
        final_list.append(i.split(" "))

    return final_list


def save_to_file(name_of_file, board):
    write_file = open(name_of_file, "w")
    board.join("\n")
    board.join(" ")
    write_file.write(board)
    write_file.close()


def main():
    current_board = []
    blank_board = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'],
                   ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
    string_board = ""
    comp_x = 0
    comp_y = 0

    print("One player battleship!")
    print("====================")
    print("")

    load_file_check = input("Would you like to load a saved game? ")
    print("")

    if load_file_check.lower() == "yes":
        save_file = input("What's the name of the file you'd like to load? ")
        try:
            current_board = load_from_file(save_file)
            line_counter = 0
            for line in current_board:
                ele_counter = 0
                for ele in line:
                    if ele == "X":
                        comp_x = int(line_counter)
                        comp_y = int(ele_counter)
                        line.remove(ele)
                        line.insert(ele_counter, "o")
                    elif ele == "_":
                        line.remove(ele)
                        line.insert(ele_counter, " ")
                    ele_counter += 1
                line_counter += 1


        except:
            current_board = blank_board
            custom_comp_ship = input("Do you want to set the location of the computer's ship?\n"
                                     "Type row,col to set or press Enter/Return to skip ")
            print("")

            try:
                comp_x = int(custom_comp_ship[0])
                comp_y = int(custom_comp_ship[2])
            except:
                print("..generating random coordinates.")
                comp_x = random.randint(0, 4)
                comp_y = random.randint(0, 4)
    else:
        current_board = blank_board
        custom_comp_ship = input("Do you want to set the location of the computer's ship?\n"
                                 "Type row,col to set or press Enter/Return to skip ")
        print("")

        try:
            comp_x = int(custom_comp_ship[0])
            comp_y = int(custom_comp_ship[2])
        except:
            print("..generating random coordinates.")
            comp_x = random.randint(0, 4)
            comp_y = random.randint(0, 4)

    quit_loop = False

    while not quit_loop:
        string_board = ""

        for line in current_board:
            for ele in line:
                string_board += str(ele)
                string_board += " "
            string_board += "\n"

        print(string_board)

        user_choice = input("(s)ave, (q)uit, or enter a row and column ")
        print("")

        try:
            if user_choice == "q":
                break

            elif user_choice == "s":
                saving_board = current_board.copy()

                for line in saving_board:
                    ele_counter = 0
                    for ele in line:
                        if ele == " ":
                            line.remove(ele)
                            line.insert(ele_counter, "_")
                        ele_counter += 1

                line_counter = 0
                for line in saving_board:
                    ele_counter = 0
                    for ele in line:
                        if line_counter == comp_x and ele_counter == comp_y:
                            line.remove(ele)
                            line.insert(ele_counter, "X")
                        ele_counter += 1
                    line_counter += 1

                saving_string_board = ""
                for line in saving_board:
                    for ele in line:
                        saving_string_board += str(ele)
                        saving_string_board += " "
                    saving_string_board += "\n"

                save_to_file("save.txt", saving_string_board)

                line_counter = 0
                for line in current_board:
                    ele_counter = 0
                    for ele in line:
                        if ele == "X":
                            comp_x = int(line_counter)
                            comp_y = int(ele_counter)
                            line.remove(ele)
                            line.insert(ele_counter, "o")
                        elif ele == "_":
                            line.remove(ele)
                            line.insert(ele_counter, " ")
                        ele_counter += 1
                    line_counter += 1

            elif int(user_choice[0]) == comp_x and int(user_choice[2]) == comp_y:
                print("The boat was at row {} and column {}".format(str(comp_x), str(comp_y)))
                print("YOU WON!!!!!!")

                line_counter = 0
                for line in current_board:
                    ele_counter = 0
                    for ele in line:
                        if line_counter == comp_x and ele_counter == comp_y:
                            line.remove(ele)
                            line.insert(ele_counter, "X")
                        ele_counter += 1
                    line_counter += 1

                string_board = ""
                for line in current_board:
                    for ele in line:
                        string_board += str(ele)
                        string_board += " "
                    string_board += "\n"

                print("")
                print(string_board)

                quit_loop = True

            else:
                user_x = int(user_choice[0])
                user_y = int(user_choice[2])
                del current_board[user_x][user_y]
                current_board[user_x].insert(user_y, " ")

        except:
            print("That's not valid! Game quitting. ")
            break


if __name__ == "__main__":
    main()
