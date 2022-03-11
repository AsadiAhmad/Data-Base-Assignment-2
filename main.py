def get_user_list(counts):
    list_user = []
    for counter in range(counts):
        dictionary = {}
        user_name = input("Enter user.name: ")
        user_age = int(input("Enter user.age: "))
        dictionary["name"] = user_name
        dictionary["age"] = user_age
        list_user.append(dictionary)
    return list_user

def search_username(name):
    result = False
    for temp in user_list:
        if temp["name"] == name:
            print(temp["age"])
            result = True
    if not result:
        print("There is no user with given name!")


if __name__ == '__main__':
    user_count = int(input("Enter users counts: "))
    user_list = get_user_list(user_count)
    search = input("Enter name to search: ")
    search_username(search)

