def findMedian(root):
    temp = []
    
    def inorder(root, temp):
        if root:
            inorder(root.left, temp)
            temp.append(root.data)
            inorder(root.right, temp)
    
    inorder(root, temp)
    
    mid = len(temp) // 2
    
    if len(temp) % 2 != 0:
        return temp[mid]
        
    if (temp[mid] + temp[mid - 1]) // 2 == (temp[mid] + temp[mid - 1]) / 2:
        return (temp[mid] + temp[mid - 1]) // 2
    else:
        return (temp[mid] + temp[mid - 1]) / 2