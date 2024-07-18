import json

type json_card_structure = dict[str, str | int]
type json_topic_structure = list[json_card_structure]


def read_topic(path: str) -> json_topic_structure:
    with open(path, "r", encoding="utf-8") as fstream:
        json_topic: json_topic_structure = json.load(fstream)  # TODO validate
    return json_topic
