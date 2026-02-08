class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ll = []
        if root:
            ll.append(root.val)

        def combine(root, ll):
            if root.left and root.right:
                ll.append(round((root.left.val + root.right.val)/2, 5))
            combine(root.left)
            combine(root.right)

        combine(root)
        return ll
            
            
# from collections import deque

# class Solution:
#     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#         if not root:
#             return []
        
#         result = []
#         queue = deque([root])  # 初始化 Queue，先把根節點放進去
        
#         while queue:
#             level_sum = 0
#             level_count = len(queue)  # 關鍵：先記錄這一層有幾個節點
            
#             # 這個迴圈只會跑「當前這一層」的次數
#             for _ in range(level_count):
#                 node = queue.popleft() # 取出節點
#                 level_sum += node.val  # 累加數值
                
#                 # 把下一層的小孩加入 Queue 排隊
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
            
#             # 這一層跑完了，計算平均
#             result.append(level_sum / level_count)
            
#         return result