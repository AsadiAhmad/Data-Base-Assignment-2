def get_user_list(counts):
    list_user = []
    for counter in range(counts):
        dictionary = {}
        user_name = input("Enter user.name:")
        user_age = int(input("Enter user.age:"))
        dictionary[user_name] = user_age
        list_user.append(dictionary)
    return list_user


if __name__ == '__main__':
    user_count = int(input("Enter users counts:"))
    user_list = get_user_list(user_count)
    print(user_list)
