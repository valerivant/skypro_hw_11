import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidate = json.load(file)
    return candidate


def get_candidate(candidate_id):
    for candidate in load_candidates():
        if candidate_id == candidate['id']:
            return candidate


def get_candidate_by_name(candidate_name):
    candidates_name = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            candidates_name.append(candidate['name'])
    return f'{", ".join(candidates_name)}'


def get_by_skill(skill_name):
    candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].split(", "):
            candidates.append(candidate['name'])
    return f'{", ".join(candidates)}'
