import json
from os.path import exists


# Write to JSON file indented.
def write_json(file_data, file_name):
    with open(file_name, "w") as f:
        json.dump(file_data, f, indent=4)


# This is the menu function that contain the user information to be inserted
def menu():
    # TODO - input can't be empty

    category_input = input("Enter a category for this product: ")
    name_input = input("Enter a name for this product: ")
    color_input = input("Enter a color for this product: ")
    size_input = input("Enter a size for this product: ")
    price_input = float(input("Enter a price for this product: "))

    return category_input, name_input, color_input, size_input, price_input


def main():
    # Data to be written
    # This variable have a small portion of json format will create the outline of the json file.
    if not exists("sample.json"):
        dictionary = {
            "product": []
        }

        with open("sample.json", "w") as outfile:
            json.dump(dictionary, outfile, indent=4)

    print("----Add a product to a JSON file----")
    category_input, name_input, color_input, size_input, price_input = menu()
    with open("sample.json") as jsonFile:
        data = json.load(jsonFile)
        temp = data["product"]
        new_id = len(data["product"])
        new_data = {
                "product id": new_id + 1,
                "category": category_input,
                "name": name_input,
                "color": color_input,
                "size": size_input,
                "price": price_input
            }
        temp.append(new_data)
        write_json(data, "sample.json")
        print("Your product has been added to \"sample.json\".")


main()
