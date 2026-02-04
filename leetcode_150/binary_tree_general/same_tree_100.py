class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pl = []
        ql = []

        def re(rr, ll):
            if not rr:
                ll.append(None)
                return
            ll.append(rr.val)

            re(rr.left, ll)
            re(rr.right, ll)                
        
        re(p,pl)
        re(q,ql)

        return pl == ql