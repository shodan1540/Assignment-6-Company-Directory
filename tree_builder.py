class EmployeeNode:
    '''
    This class represents one employee in the company tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): Their left report (if any).
        right (EmployeeNode): Their right report (if any).
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    The TeamTree class is used to handle the whole structure
    of employees and their hierarchy.
    It keeps track of who reports to who and allows new
    employees to be added under the right person.
    '''
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Start at root if not given
        if current_node is None:
            current_node = self.root

        if current_node is None:
            print("⚠️ No team lead found. Please add a root employee first.")
            return False

        # Found the manager, now try to attach the employee
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                    return True
                else:
                    print(f"⚠️ The LEFT side of {manager_name} is already taken.")
                    return False
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                    return True
                else:
                    print(f"⚠️ The RIGHT side of {manager_name} is already taken.")
                    return False
            else:
                print("⚠️ Please enter either 'left' or 'right' for the side.")
                return False

        # Keep searching if we didn't find the manager yet
        inserted = False
        if current_node.left:
            inserted = self.insert(manager_name, employee_name, side, current_node.left)
        if not inserted and current_node.right:
            inserted = self.insert(manager_name, employee_name, side, current_node.right)

        # If the manager never shows up
        if not inserted and current_node == self.root:
            print(f"⚠️ Could not find a manager named '{manager_name}'.")
        return inserted

    def print_tree(self, node=None, level=0):
        # Start from root
        if node is None:
            node = self.root
            if node is None:
                print("⚠️ There’s no team structure yet.")
                return

        print("    " * level + f"- {node.name}")

        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ A team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")
        
        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ").lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option, try again.")


# ---------------------------------------------------------------------- #
# Design Memo: #
# #
# For this assignment, I built a small program that uses a custom tree # 
# to organize a company’s reporting structure. Each employee is one # 
# node, and the TeamTree keeps track of how they connect. The root is # 
# always the team lead, and everyone else gets inserted under someone. #
# #
# The recursive insert() was the most interesting part because it had # 
# to “walk” through the tree looking for the right manager before # 
# deciding where to put the new employee. Once it finds the manager, it # 
# checks if that left or right spot is empty and puts the new person # 
# there. If not, it prints a little warning. It took some trial and # 
# error to make sure the recursion didn’t stop too early or miss # 
# branches. #
# #
# One issue I ran into was when trying to add people before there was # 
# even a root. I had to add checks to prevent that. Also, making sure # 
# the user types "left" or "right" correctly was a small detail that # 
# caused bugs at first. #
# #
# Trees like this are great when you need to show relationships instead # 
# of just storing data. A list or dictionary could hold the names, but # 
# a tree makes it easy to see the structure visually, like who reports # 
# to who. Recursion just makes it more natural to navigate since every # 
# employee can have their own sub-tree of people below them. #
# ---------------------------------------------------------------------- #
