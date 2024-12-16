# 20241216-white_elephant-gist

**Gist file**: [https://gist.github.com/rjvitorino/a71c48ce2974426526293e06116ae9c7](https://gist.github.com/rjvitorino/a71c48ce2974426526293e06116ae9c7)

**Description**: Cassidy's interview question of the week: a white elephant gift exchange class that simulates the game. It generates a sequence of random but valid gift-opening and gift-stealing moves for n participants, tracks steal counts and frozen gifts, and ends the game when everyone has a gift.

## white_elephant.py

```Python
from typing import Dict, Optional
import random


class WhiteElephantGame:
    """
    A simulation of the White Elephant Gift Exchange game. https://www.whiteelephantrules.com/

    Overview:
        The game involves players taking turns to either open a new gift from a pool of unopened gifts
        or steal a gift already opened by another player. Each gift can only be stolen a limited number
        of times (defined by max_steals). The game ends when all gifts have been opened and each player
        has a gift.

    Mapping to Class:
        - Players:
            Represented as integers from 0 to num_players - 1.
            The current turn order is managed by `current_player_order`.
        - Gifts:
            Represented as integers from 0 to num_players - 1.
            Ownership is tracked using `gift_owners` and `players_with_gifts`.
            Gifts yet to be opened are stored in `unopened_gifts`.
        - Stealing:
            The count of steals for each gift is tracked by `steal_counts`.
        - Turns:
            The turn logic is handled using `current_player_index`, with randomized order determined
            at the start of the game.

    Methods:
        - next_move(): Determines the next action in the game based on the state of gifts and players.
        - _open_gift(): Handles logic for a player opening a gift.
        - _steal_gift(): Handles logic for a player stealing a gift from another player.
        - _end_game(): Finalizes the game and returns the distribution of gifts among players.

    """

    def __init__(self, num_players: int, max_steals: int = 3) -> None:
        """
        Initialize the White Elephant Game.

        Args:
            num_players (int): Number of participants in the game.
            max_steals (int): Maximum number of times a single gift can be stolen. Defaults to 3.
        """
        self.num_players = num_players
        self.max_steals = max_steals
        # Gifts are represented by indices 0 to num_players - 1
        self.gifts = list(range(num_players))
        self.steal_counts: Dict[int, int] = {gift: 0 for gift in self.gifts}
        # Tracks who owns each gift
        self.gift_owners: Dict[int, Optional[int]] = {gift: None for gift in self.gifts}
        # Tracks players' current gifts
        self.players_with_gifts: Dict[int, Optional[int]] = {
            player: None for player in range(num_players)
        }
        self.unopened_gifts = set(self.gifts)
        self.current_player_order = list(range(num_players))
        # Randomize player order
        random.shuffle(self.current_player_order)
        # Tracks the turn order
        self.current_player_index = 0

    def next_move(self) -> str:
        """
        Simulate the next move in the game.

        Returns:
            str: Description of the move.
        """
        # Check if all gifts have been opened and all players have a gift
        if not self.unopened_gifts and all(
            gift is not None for gift in self.players_with_gifts.values()
        ):
            return self._end_game()

        current_player = self.current_player_order[self.current_player_index]

        # Check for stealable gifts
        stealable_gifts = [
            gift
            for gift, owner in self.gift_owners.items()
            if owner is not None and self.steal_counts[gift] < self.max_steals
        ]

        # Decide whether to steal or open a gift (50/50 chance)
        if stealable_gifts and (not self.unopened_gifts or random.random() < 0.5):
            # If there are gifts that can be stolen, AND
            # (either there are no unopened gifts left OR we get heads on a coin flip),
            # then proceed with the action
            return self._steal_gift(current_player)

        # If the current player doesn't have a gift and there are unopened gifts, open one
        if self.players_with_gifts[current_player] is None and self.unopened_gifts:
            return self._open_gift(current_player)

        # If the current player already has a gift, move to the next player
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        return self.next_move()

    def _open_gift(self, current_player: int) -> str:
        """
        Current player opens an unopened gift.

        Returns:
            str: Description of the move.
        """
        gift = random.choice(list(self.unopened_gifts))
        self.unopened_gifts.remove(gift)
        self.gift_owners[gift] = current_player
        self.players_with_gifts[current_player] = gift
        result = f"Person {current_player} opened gift {gift}"
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        return result

    def _steal_gift(self, current_player: int) -> str:
        """
        Current player steals a gift from another player.

        Returns:
            str: Description of the move.
        """
        stealable_gifts = [
            gift
            for gift, owner in self.gift_owners.items()
            if owner is not None and self.steal_counts[gift] < self.max_steals
        ]

        gift = random.choice(stealable_gifts)
        previous_owner = self.gift_owners[gift]

        self.players_with_gifts[previous_owner] = None
        self.gift_owners[gift] = current_player
        self.players_with_gifts[current_player] = gift
        self.steal_counts[gift] += 1

        result = (
            f"Person {current_player} stole gift {gift} from person {previous_owner}"
        )
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        return result

    def _end_game(self) -> str:
        """
        End the game and return the final distribution.

        Returns:
            str: Final distribution of gifts.
        """
        final_distribution = {
            f"person {player}": gift for player, gift in self.players_with_gifts.items()
        }
        return f"Game Over! Final distribution: {final_distribution}"


if __name__ == "__main__":
    num_players = 4
    game = WhiteElephantGame(num_players)

    while True:
        move = game.next_move()
        print(move)
        if "Game Over!" in move:
            break

```