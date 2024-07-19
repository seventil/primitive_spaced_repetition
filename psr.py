import json

type question = str
type answer = str
type priority = int


class JsonTopicKey(str):
    ACCEPTABLE_KEYS = {"Priority", "Question", "Answer"}

    def __new__(cls, *args, **kw):
        if args[0] not in cls.ACCEPTABLE_KEYS:
            raise ValueError(f"JSON Topic key <{args[0]}> is unexpected")
        return str.__new__(cls, *args, **kw)


type json_card_structure = dict[JsonTopicKey, question | answer | priority]
type json_topic_structure = list[json_card_structure]

DEFAULT_ENCODING = "utf-8"
PRIORITY_PATH = "priority.json"


def read_topic(path: str) -> json_topic_structure:
    with open(path, "r", encoding=DEFAULT_ENCODING) as fstream:
        json_topic: json_topic_structure = json.load(fstream)  # TODO validate
    return json_topic
