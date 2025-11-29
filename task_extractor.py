import spacy
import re
from dateutil.parser import parse

nlp = spacy.load("en_core_web_sm")

PRIORITY_WORDS = {
    "critical": "Critical",
    "urgent": "High",
    "high priority": "High",
    "important": "Medium",
    "can wait": "Low",
    "low priority": "Low"
}

def extract_deadline(sentence):
    patterns = [
        r"tomorrow",
        r"today",
        r"next\s+\w+",
        r"by\s+\w+day",
        r"by\s+[\w\s]+",
        r"before\s+\w+day"
    ]
    for p in patterns:
        match = re.search(p, sentence, re.I)
        if match:
            return match.group()
    return None


def extract_priority(sentence):
    for word, level in PRIORITY_WORDS.items():
        if word in sentence.lower():
            return level
    return "Medium"


def extract_tasks(text):
    doc = nlp(text)
    tasks = []
    
    for sent in doc.sents:
        s = sent.text.strip()
        
        # find verbs (actions)
        for token in sent:
            if token.pos_ == "VERB":
                task = {
                    "task": s,
                    "action": token.lemma_,
                    "deadline": extract_deadline(s),
                    "priority": extract_priority(s),
                    "assigned_to": None,
                    "dependency": None
                }
                tasks.append(task)
                break

    return tasks
