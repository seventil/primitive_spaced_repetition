import json
from collections import deque

type json_card_key = str
type question = str
type answer = str
type priority = int
type json_card_structure = dict[json_card_key, question | answer | priority]

JSON_CARD_PRIORITY_KEY = "Priority"
JSON_CARD_QUESTION_KEY = "Question"
JSON_CARD_ANSWER_KEY = "Answer"
JSON_CARD_STRUCTURE = {
    JSON_CARD_PRIORITY_KEY: int,
    JSON_CARD_QUESTION_KEY: str,
    JSON_CARD_ANSWER_KEY: str,
}

type json_topic_structure = list[json_card_structure]

DEFAULT_ENCODING = "utf-8"
PRIORITY_PATH = "priority.json"


def read_topic(path: str) -> json_topic_structure:
    with open(path, "r", encoding=DEFAULT_ENCODING) as fstream:
        json_topic: json_topic_structure = json.load(fstream)
        for card in json_topic:
            for key, value in card.items():
                assert key in JSON_CARD_STRUCTURE
                assert isinstance(value, JSON_CARD_STRUCTURE[key])

    return json_topic


class CardQueue:
    def __init__(self, json_topic):
        self.q: deque = deque()
        for card in json_topic:
            self.place(card)

    def place(self, card):
        priority = card[JSON_CARD_PRIORITY_KEY]
        if priority >= len(self.q):
            self.q.append(card)
        else:
            self.q.insert(priority, card)

    def peek_next_card(self):
        return self.q[0]

    def replace(self, new_priority):
        current_card = self.q.popleft()
        current_card[JSON_CARD_PRIORITY_KEY] = new_priority
        self.place(current_card)


def main():
    read_path = (
        "topics/kekus.json"  # TODO build path to topics defaulting to topics/*.json
    )
    card_queue = CardQueue(read_topic(read_path))

    # TODO add loop with user input
    current_card = card_queue.peek_next_card()

    # TODO change priority and commit the replace


if __name__ == "__main__":
    main()
