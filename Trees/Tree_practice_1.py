class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
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
    
def buildtree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.addChild(TreeNode('Windows'))
    laptop.addChild(TreeNode('Mac'))

    mobile = TreeNode('Mobile')
    mobile.addChild(TreeNode('Android'))
    mobile.addChild(TreeNode('IOS'))

    tv = TreeNode('TV')
    tv.addChild(TreeNode('Samsung'))
    tv.addChild(TreeNode('LG'))

    root.addChild(laptop)
    root.addChild(mobile)
    root.addChild(tv)

    return root

if __name__ == '__main__':
    root = buildtree()
    root.printTree()