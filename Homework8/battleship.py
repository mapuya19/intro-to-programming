# Matthew Apuya
# 11/19/19
# CSCI-UA.00003-001

"""
battleship.py
=====

Write a simplified one player version of Battleship.  In this version of 
Battleship, the computer hides a ship in a 5 x 5 grid.  The player must find
the ship by inputting row and column pairs.  If the player finds the ship,
the player wins. The player has unlimited turns! Additionally, the player 
can save or load their progress to a file (though looking at the file will 
reveal the location of the ship). 

1. Implement the following functions:
   a. load_from_file(name_of_file)
      -----
      parameter - name_of_file: str
      returns - a tuple containing:
      * a list of lists representing the board
      * and a number representing the number of moves so far

      This function will read a file based on the string passed in as 
      name_of_file. The format of the file will be:

o o o o o
o o X o o
o o o o o
o _ o o o
o o _ o o
      
      * o represents a "cell" that has not been revealed yet
      * _ represents a "cell" that has been revealed and does not contain
          the computer's ship
      * X represents a "cell" that has not been revealed yet

      The function will return a nested list based on the data in the file:

      * each line will be a sublist, and each symbol will be an element in
        the sublist
      * given the example file above, this function should return:

        [['o', 'o', 'o', 'o', 'o'], 
         ['o', 'o', 'X', 'o', 'o'], 
         ['o', 'o', 'o', 'o', 'o'], 
         ['o', '_', 'o', 'o', 'o'], 
         ['o', 'o', '_', 'o', 'o']]

      example call:

in_fn = 'save.txt'
board = load_from_file(in_fn) # board will be a nested list

   b. save_to file(name_of_file, board)
      -----
      parameter - name_of_file: str
      returns - no return value

      This function will take a board in the nested list format produced by 
      the function, load_from_file... and write it out to the file specified by
      name_of_file, again, in the same format as load_from_file.

      example call:

# board is a nested list
out_fn = 'out.txt'
save_to_file(out_fn, board) # no return value, but file out.txt is created

2. Create a main function:

   def main():
   
   Call the function at the end of your file in an if __name__ == '__main__':
   statement.

   This main function will contain all the code for your actual game. Start by 
   setting up the game based on answers from the user:
   
   * ask the user if they'd like to load a file:

     Would you like to load a saved game?
     > YES

   * answering 'yes' in any casing will result in another question:

     What's the name of the file you'd like to load?
     > some_file.txt

   * if the file doesn't exist (causes a runtime error) or if the user
     did not say yes to the previous question, then create a list of 
     5 sublists, with each sublist containing the string 'o' 5 times
   * if the file is successfully read, then use the nested list from the
     file as the board for your game (use the function you defined 
     earlier to do this... and if it's helpful, an exception in a function 
     can be caught by a try except surrounding the function call)

3. The computer's ship only occupies one "square" (unlike the regular version 
   of Battleship). If the board was generated rather than read from a file,
   place the ship in a random location on the board. However, before this is 
   done, to help make testing your game easier, your program MUST ASK IF THE 
   PLAYER WANTS to explicitly set the location of the computer's ship. 
   
   (only if the board is not read from the file)
   Do you want to set the location of the computer's ship? 
   Type row,col to set or press ENTER/RETURN to skip 
   >

   If the player types in a row and column (for example 1,2), then the 
   computer's ship is placed at that location. No validation is required; you
   can assume that the user will always type in a row and column or they will 
   type in nothing. If the player doesn't type in anything and just presses 
   ENTER/RETURN (in which case input will return an empty string, ""), the 
   computer will generate a random row and column for the location of its ship 
   (both are 0 through 4).

4. Display the board... and then ask the player for a command.

   The board SHOULD NOT BE DISPLAYED AS LISTS... instead, print out a
   formatted version of the board where the uncovered empty "cells" are 
   spaces rather than '_' and the location of the ship, the 'X', is replaced
   by an 'o' to show that the "cell" has not been revealed yet. For example,
   the board:

        [['o', 'o', 'o', 'o', 'o'], 
         ['o', 'o', 'X', 'o', 'o'], 
         ['o', 'o', 'o', 'o', 'o'], 
         ['o', '_', 'o', 'o', 'o'], 
         ['o', 'o', '_', 'o', 'o']]
    
    ... will be displayed as:

        o o o o o
        o o o o o
        o o o o o
        o   o o o
        o o   o o

   Underneath the board, ask the user for a a row and a column (both are 0-4), 
   separated by a comma... for example: 1,2 means row 1, column 2... or the 
   letter q or s. Your program MUST ACCEPT ONLY THE INPUTS specified above:

   

   a. If the input is just q, the game ends.
   b. If the input is just s, ask the user for a name of a file, and
      write the board to the file (use the function you defined earlier):

      (s)ave, (q)uit or enter a row and column 
      >
    
   c. If the input is not l, q or a row and column, display the board and
      ask for a command again.

5. The row and column input is either a hit or a miss.
   a. If the input uncovers the ship, the player wins and the game ends.
   b. If the input is a miss, the 'o' board's display is replaced with " " (a 
      space) so that the user can see which rows and columns they have already
      tried.

6. If the user wins, display the board with one last, with an X displaying the
   last move / location of the computer's "boat". See the output at the end of 
   this comment for a sample game.

Partial credit will be given!


Sample Output:
-----

One player battleship!
====================


Would you like to load a saved game?
> no

Do you want to set the location of the computer's ship? 
Type row,col to set or press ENTER/RETURN to skip 
> 2,3

o o o o o
o o o o o
o o o o o
o o o o o
o o o o o

(s)ave, (q)uit or enter a row and column 
> 1,1


o o o o o
o   o o o
o o o o o
o o o o o
o o o o o
(s)ave, (q)uit or enter a row and column 
> 2,3

The boat was at row 2 and column 3
YOU WON!!!!

o o o o o
o   o o o
o o o X o
o o o o o
o o o o o
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
