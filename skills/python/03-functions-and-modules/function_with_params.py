def contains_purple(*args):
    for arg in args:
        if isinstance(arg, str) and arg.lower() == "purple":
            return True
    return False

print(contains_purple(34, "blue", "green"))

def favorite_color(**kwargs):
    for key, value in kwargs.items():
        if value.lower() == "purple":
            return f"{key} loves purple"
    return "No one loves purple"

print(favorite_color(color="purple"))