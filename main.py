if __name__ == '__main__':
    user_list = []
    user_count = int(input("Enter users counts:"))

    for counter in range(user_count):
        dictionary = {}
        user_name = input("Enter user.name:")
        user_age = int(input("Enter user.age:"))
        dictionary[user_name] = user_age
        user_list.append(dictionary)

    print(user_list)
