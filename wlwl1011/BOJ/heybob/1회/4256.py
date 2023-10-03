import sys
input = lambda : sys.stdin.readline().rstrip('\r\n')

def toPostorder(preorder,inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0],end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')   
        return

    root_idx = inorder.index(preorder[0]) 
    left_in = inorder[0:root_idx]
    left_pre = preorder[1:1+len(left_in)]
    toPostorder(left_pre, left_in)

    right_in = inorder[root_idx+1:]
    right_pre = preorder[1+len(left_in):]
    toPostorder(right_pre, right_in)

    print(preorder[0],end=' ')

for _ in range(int(input())):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    toPostorder(preorder,inorder)
    print()
    