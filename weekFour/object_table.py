class Table:

    # Constructor
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.insert_col = ""
        self.col_index = -1
        self.row_index = -1

    # Print a table with the constructor rows and columns
    def print_table(self):
        col_count = 0
        row_count = 0

        print("<table>")

        while row_count < self.row:
            print("<tr>")
            while col_count < self.column:
                if row_count == self.row_index and col_count == self.col_index:
                    print("<td>" + self.insert_col + "</td>")
                    col_count += 1
                else:
                    print("<td>test</td>")
                    col_count += 1
            print("</tr>")
            row_count += 1
            col_count = 0

        print("</table>")

    # Set rows how many columns
    def set_row(self, row):
        self.row = row

    # Set column how many columns
    def set_column(self, column):
        self.column = column

    # Insert a string to a specific row and column
    def insert_column(self, insert_col, row_index, col_index):
        self.insert_col = insert_col
        self.row_index = row_index
        self.col_index = col_index


def main():
    test = Table(2, 3)
    print(test.row, test.column)
    test.set_row(3)
    test.set_column(5)
    test.insert_column("Hello World", 0, 1)
    test.insert_column("Welcome to MyProfile", 0, 2)
    print(test.row, test.column)
    test.print_table()


main()


