from bson import json_util
import json
from sys import stdout, stderr, exit

state = {}
feedback = []


def addFeedback(summary, detail=''):
    feedback.append((summary, detail))


def failed(message):
    stderr.write(message)
    exit(1)


def complete():
    stdout.write(json.dumps(state, default=json_util.default))
    stderr.write(json.dumps(feedback, default=json_util.default))
