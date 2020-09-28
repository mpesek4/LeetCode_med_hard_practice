
# https://leetcode.com/problems/accounts-merge/

def accountsMerge(self,accounts):
    
        dp = {}
        merge_tuples = []
        # set up an adjacency list and do a DFS to merge accounts with overlapping emails
        for idx,acc in enumerate(accounts):
            for i in range(1,len(acc)):
                if acc[i] in dp:
                    dp[acc[i]].append(idx)
                else:
                    dp[acc[i]] = [idx]
        explored = {}
        res = []

        def dfs(idx, emails):
            if idx in explored:
                return
            explored[idx] = 1
            for j in range(1, len(accounts[idx])):
                email = accounts[idx][j]
                emails.add(email)
                for child in dp[email]:
                    dfs(child,emails)

        for i, account in enumerate(accounts):
            if i in explored:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res