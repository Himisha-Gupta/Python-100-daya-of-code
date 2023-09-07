def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return #can return empty return statement
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}" #end of the function


print(format_name("" , ""))
