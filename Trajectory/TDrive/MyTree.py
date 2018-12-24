class node:

    def __init__(self, data):
        self._data = data
        self._children = []
        self._count = 0

    def getdata(self):
        return self._data

    def getcount(self):
        return self._count

    def getchildren(self):
        return self._children

    def add(self, node):
        self._children.append(node)



    def go(self, data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None

class tree:

    def __init__(self):
        self._head = node('Root')


    def getHead(self):
        return self._head

    def linktohead(self, node):
        self._head.add(node)


    def Insert(self,path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                cur.add(node(step))
            cur = cur.go(step)
            cur._count+=1

    def search(self, path):
        cur = self._head
        # print(cur._data)
        for step in path:
            if cur.go(step) == None:
                return "no"
            else:
                cur = cur.go(step)
        return cur._count

    def getNodechildrenCount(self,path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return "no"
            else:
                cur = cur.go(step)
        print(cur.getdata(),"}")
        for i in cur.getchildren():
            print(i.getdata(),",",i.getcount())

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return ""
        if not root.getchildren():
            return root.getdata()
        result = root.getdata()
        # print(result)
        for child in root.getchildren():
            result += self.preorder(child)
        return result

    def preorderYou(self, root):

        if not root:
            return ""
        if not root.getchildren():
            return root.getdata()
        if root.getcount()==0:
            result = ""
        else:
            result = root.getdata()
        # result = root.getdata();
        # print(result)
        for child in root.getchildren():
            result += self.preorder(child)
        return result

# tree = tree()
# tree.Insert("abcd")
# tree.Insert("abce")
# tree.Insert("abf")
# tree.Insert("ag")


# print(tree.preorder(tree.getHead()))