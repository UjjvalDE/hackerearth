class Solution:
    def findChampionship(self, rankings):
        n = len(rankings)
        champion = None
        max_points = 0
        for i in range(n):
            points = sum(1 << k for k in range(n) if rankings[i][k] == 'win')
            if points > max_points:
                max_points = points
                champion = i + 1
        return champion