import json
import re

def load_team(path=r"C:\Users\dhara\OneDrive\Desktop\data\team.json"):
    with open(r"C:\Users\dhara\OneDrive\Desktop\data\team.json") as f:
        return json.load(f)

def match_member(task_desc, team):
    task_lower = task_desc.lower()
    best_member = None
    score = 0

    for member in team:
        member_score = 0
        for skill in member["skills"]:
            if skill.lower() in task_lower:
                member_score += 2
        if member["role"].lower() in task_lower:
            member_score += 1

        if member_score > score:
            score = member_score
            best_member = member["name"]

    return best_member


def assign_tasks(tasks, team):
    for task in tasks:
        task["assigned_to"] = match_member(task["task"], team)

        # dependency detection
        if "depends on" in task["task"].lower():
            dep = re.findall(r"task\s*#\d+", task["task"], re.I)
            if dep:
                task["dependency"] = dep[0]
    return tasks
