from os import name as os_name


def path_checker(path_to_save):
    if len(path_to_save) < 1:
        return path_to_save
    else :
        if path_to_save[-1] != "\\" or path_to_save[-1] != "/":
            if os_name == "nt":
                path_to_save += "\\"
                return path_to_save
            else:
                path_to_save += "/"
                return path_to_save
        else:
            return path_to_save