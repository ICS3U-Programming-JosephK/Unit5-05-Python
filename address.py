#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: December 06
# This program calculates math operations based on user's choice


# Defining the function that format the address
# Default value for apartment
def format_address(
    address,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):

    formatted = "{}\n{} {}\n{} {} {}".format(
        address, street_number, street_name, city, province, postal_code
    )

    formatted_with_apartment_num = "{}\n{} {} {}\n{} {} {}".format(
        address,
        street_number,
        apartment_number,
        street_name,
        city,
        province,
        postal_code,
    )

    # Apartment is optional, hence in case default value...
    if apartment_number == None:
        return formatted
    else:
        return formatted_with_apartment_num


if __name__ == "__main__":
    # Getting the user input
    user_fullname = input("Enter a your full name: ")
    user_street_number = input("Enter a street number: ")
    user_apartment_number = input(
        "Enter a apartment number if any. (Press enter to skip this): "
    )
    user_street_name = input("Enter a street name: ")
    user_city = input("Enter a city: ")
    user_province = input(
        "Enter a province (as a abbreviation, EX: ON, AB, BC, QC, ect.) : "
    )
    user_postal_code = input("Enter a postal_code: ")

    formatted_address = format_address(
        user_fullname.upper(),
        user_street_number.upper(),
        user_street_name.upper(),
        user_city.upper(),
        user_province.upper(),
        user_postal_code.upper(),
        user_apartment_number,
    )
    print("")
    print(formatted_address)
