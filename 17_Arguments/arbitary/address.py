def print_address(**kwargs):
    # for key in kwargs.keys():
    #         print(key, end=" ")
    # print()
    # for val in kwargs.values():
    #     print(val, end=" ")

    for key,val in kwargs.items():
        print(f"{key}: {val}")

print_address(street="123 Fake St.",
                apt="100",
                city="Detroit",
                state="MI",
                zip="54321")