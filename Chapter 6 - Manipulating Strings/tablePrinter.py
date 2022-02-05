# Chapter 6 - Manipulating Strings
# tablePrinter.py - Print list of lists of strings in a table

def print_table(table):
    longest = [0, 0, 0]
    for i in range(4):
        for j in range(3):
            if len(table[j][i]) > longest[j]:
                longest[j] = len(table[j][i])

    for i in range(4):
        for j in range(3):
            print(table[j][i].rjust(longest[j], " "), end=" ")
        print("")


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

alt_table_data = [['Raspberry', 'Watermelon', 'cherries', 'Pitaya'],
                  ['Rodney ', 'Alvaro ', 'Jonathan ', 'Bob '],
                  ['Munchkin cat', 'Korat', 'Burmese cat', 'Persian cat']]

print_table(table_data)
print("")
print_table(alt_table_data)
