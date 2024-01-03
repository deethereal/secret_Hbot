from dataclasses import dataclass

from aiogram.types import Chat


@dataclass
class Parliament:
    chat: Chat
    num_voters: int

    def __post_init__(self):
        self.is_voting = False
        self.positive_votes = 0
        self.negative_votes = 0
        self.president_candidate = None
        self.chancellor_candidate = None
        self.voted_users = set()

    def start_voting(self, president: str, chancellor: str):
        self.is_voting = True
        self.positive_votes = 0
        self.negative_votes = 0
        self.voted_users = set()
        self.president_candidate = president
        self.chancellor_candidate = chancellor

    def end_voting(self):
        self.is_voting = False
        if self.positive_votes > self.negative_votes:
            ending = (
                f"@{self.president_candidate} становится <b>президентом</b>, "
                f"а @{self.chancellor_candidate} <b>канцлером</b>!"
            )
            symbol = "✅"
        else:
            ending = f"@{self.president_candidate} и @{self.chancellor_candidate} <b>не были выбраны</b>!"
            symbol = "❌"

        return symbol + " Голосование завершено!\nВ результате " + ending
