class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_counts = defaultdict(int)
        
        for winner, loser in matches:
            loss_counts[winner] 
            loss_counts[loser] += 1
        
        no_loss = [player for player, losses in loss_counts.items() if losses == 0]
        one_loss = [player for player, losses in loss_counts.items() if losses == 1]
        
        return [sorted(no_loss), sorted(one_loss)]
