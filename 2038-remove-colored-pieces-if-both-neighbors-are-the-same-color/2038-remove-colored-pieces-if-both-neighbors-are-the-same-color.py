class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_turn = 0
        bob_turn = 0
        prev_color = ''
        same_count = 0
        for color in colors:
            if prev_color == color:
                same_count += 1
            else:
                count = same_count - 1 if same_count > 1 else 0
                if prev_color == 'A':
                    alice_turn += count
                else:
                    bob_turn += count
                same_count = 0
            prev_color = color
        count = same_count - 1 if same_count > 1 else 0
        if prev_color == 'A':
            alice_turn += count
        else:
            bob_turn += count
        return alice_turn > bob_turn