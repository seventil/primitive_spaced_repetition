# primitive_spaced_repetition

A CLI and JSON implementation for spaced repetition.
[Spaced Repetition](https://e-student.org/spaced-repetition/) is a popular technique to memorize
information. Some popular instruments for spaced repetition use proprietary data formats.
This program's goal is to provide a CLI for a simple data format, that you don't need any 
particular program to fillout new cards, edit old cards, transfer them and practice with them.
Use this program, or any simple text editor to practice.

## JSON cards: questions and answers

The program will search the "topics" folder by default for a specified cards topic,
or you could use a full path to the file.

```python3 psr.py python```
or
```python3 psr.py topics/python.json```

The structure for one card is the following:
```
{
    "Priority": 0,
    "Question": "",
    "Answer": ""
}
```
Question and Answer are filled out by the user, Priority is managed by the program and may be ommited initially.
A topic combines cards within a list in a json file.

## PSR workflow

Run the program by specifying the topic:

```python3 psr.py python```

The program will sort the cards from the python topic by priority, and you'll see the highest priority question.
The program will prompt you to write the answer down, but you can also answer in you mind and submit an empty string.

>Filling out the answer will help you recall better.

The program will ask if you think you answered the question correctly. Y/Yes/y/N/No/n will change the priority of the card
and put it into a new place in the queue.
