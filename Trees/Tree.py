class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def buildTree():
    root = TreeNode("Electronics")

    laptop = TreeNode('laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Windows'))
    laptop.add_child(TreeNode('Linux'))

    mobile = TreeNode('mobile')
    mobile.add_child(TreeNode('Android'))
    mobile.add_child(TreeNode('IOS'))
    mobile.add_child(TreeNode('Windows'))

    tv = TreeNode('tv')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root


    
if __name__ == '__main__':
    root = buildTree()
    root.printTree()
