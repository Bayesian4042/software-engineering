
# Problem

def print_owing():
    print_banner()

    # Print details.
    print("name:", name)
    print("amount:", get_outstanding())

# Issue
## The more lines found in a method, the harder it’s to figure out what the method does. This is the main reason for this refactoring.


# Solution
def print_owing():
    print_banner()
    print_details(get_outstanding())

def print_details(name, outstanding):
    print("name:", name)
    print("amount:", outstanding)