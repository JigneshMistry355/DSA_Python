class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.employee = []
        self.boss = None

    # def __init__(self, name):
    #     self.name = name
    #     self.employee = []
    #     self.boss = None

    # def __init__(self, designation):
    #     self.designation = designation
    #     self.employee = []
    #     self.boss = None

    def addEmployee(self, Employee):
        Employee.boss = self    
        self.employee.append(Employee)

    def getLevel(self):
        level = 0
        e = self.boss
        while e:
            e = e.boss
            level += 1
        return level

    def printTree(self, choice):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + '|__' if self.boss else ''
        if choice == 'name':
            print(f'{prefix}{self.name}')
        elif choice == 'designation':
            print(f'{prefix}{self.designation}')
        else:
            print(f'{prefix}{self.name}( {self.designation} )') 
        if self.employee:
            for emp in self.employee:
                emp.printTree(choice)


def buildTree():
    
    CEO = TreeNode('Nilupul', 'CEO')

    CTO = TreeNode('Chinmay', 'CTO')
    
    Infra_head = TreeNode('Vishwa', 'Infrastructure Head')
    Infra_head.addEmployee(TreeNode('Dhaval', 'Cloud Manager'))
    Infra_head.addEmployee(TreeNode('Abhijit', 'App Manager'))

    App_head = TreeNode('Aamir', 'Application Head')

    CTO.addEmployee(Infra_head)
    CTO.addEmployee(App_head)

    HR = TreeNode('Gels', 'HR Head')
    HR.addEmployee(TreeNode('Peter', 'Recruitement Manager'))
    HR.addEmployee(TreeNode('Waqas', 'Policy Manager'))

    CEO.addEmployee(CTO)
    CEO.addEmployee(HR)

    return CEO

if __name__ == '__main__':
    root = buildTree()
    # choice = input("Enter choice")
    root.printTree('designation')
    
