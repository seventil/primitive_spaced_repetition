import json

type json_card_key = str
type question = str
type answer = str
type priority = int
type json_card_structure = dict[json_card_key, question | answer | priority]
JSON_CARD_STRUCTURE = {"Priority": int, "Question": str, "Answer": str}

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
