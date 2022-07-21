import os
import sys
import webbrowser


# Contain the style of the webpage
def css_file():
    print("These are suggested colors:\n"
          "\tcadetblue, aliceblue, coral, crimson, red, blue, etc.\n"
          "You can also use HEX values (#ff6347)")
    user_input = input("Enter the background color for this website: ")
    with open("style.css", "w") as style:
        sys.stdout = style
        print("body {\n"
              "\tbackground-color: " + user_input + ";\n"
              "\tdisplay: flex;\n"
              "\tjustify-content: center;\n" 
              "\twidth: 50vh;\n"
              "\tmargin: 0 auto 0 auto;\n"
              "\tfont-family: Arial, Helvetica, sans-serif;\n"
              "}")
        print("td {\n"
              "\tpadding: 0;\n" 
              "}")
        print("h2, h3 {\n"
              "\tmargin: 5px 0;\n"
              "}")


def add_image(user_input):

    if user_input:
        return """<img width="200px" 
            src=""" + user_input + " alt="">"""
    else:
        return("""<img width="200px" 
            src="https://www.cmzoo.org/wp-content/uploads/grizzlybear-digger.jpg" alt="">""")


def add_name(user_input):

    if user_input:
        return "<h2>" + user_input + "</h2>"
    else:
        return "<h2>Jon Due</h2>"


def add_location(user_input):
    if user_input:
        return "<h3>" + user_input + "</h3>"
    else:
        return "<h3>Seattle, Washington</h3>"


def add_bio(user_input):
    if user_input:
        return "<p>" + user_input + "</p>"
    else:
        return ("<p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical "
        "Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at "
        "Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, "
        "from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered "
        "the undoubtable source.</p>")


def make_table(row, col, user_img, user_name, user_loc, user_bio):
    col_count = 0
    row_count = 0

    print("<table>")

    while row_count < row:
        table_sections = [add_image(user_img), add_name(user_name), add_location(user_loc), add_bio(user_bio)]
        print("<tr>")
        while col_count < col:
            print("<td>" + table_sections[row_count] + "</td>")
            col_count += 1
        print("</tr>")
        row_count += 1
        col_count = 0

    print("</table>")


def main():
    print("------------Welcome to MyProfile-------------------")
    print("Lets begin!\n")
    print("-If you leave it blank, it will use default values-")
    image_in = input("Profile image:" + "\x1B[3m" + " Paste your image address or path here -> " + "\x1B[0m")
    name_in = input("Profile name:" + "\x1B[3m" + " Enter your name here -> " + "\x1B[0m")
    location_in = input("Profile location:" + "\x1B[3m" + " Enter your location here -> " + "\x1B[0m")
    bio_in = input("Profile bio:" + "\x1B[3m" + " Enter your bio here -> " + "\x1B[0m")
    css_file()

    with open("index.html", "w") as f:
        sys.stdout = f
        image_in = image_in
        name_in = name_in
        location_in = location_in
        bio_in = bio_in
        print("<!DOCTYPE html>\n")
        print("<html lang=\"en\">\n")
        print("<head>")
        print("<link rel=\"stylesheet\" href=\"style.css\">")
        print("<title>Document</title>")
        print("</head>")
        print("<body>")
        make_table(4, 1, image_in, name_in, location_in, bio_in)
        print("</body>")
        print("</html>")
    filename = 'file:///' + os.getcwd() + '/' + 'index.html'
    webbrowser.open_new_tab(filename)


main()
