class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = j = pairs = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                pairs += 1
                i += 1
                j += 1
            else:
                j += 1  # Skip the trainer

        return pairs
