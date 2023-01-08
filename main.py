from flask import Flask, request, render_template

from utils import load_candidates, get_candidate_by_name, get_candidate, get_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    items = load_candidates()
    return render_template('list.html', items=items)


@app.route('/candidate/<int:position>')
def candidate_page(position):
    item = get_candidate(position)
    return render_template('card.html', item=item)


@app.route('/search/<candidate_name>')
def search_by_name_page(candidate_name):
    item = get_candidate_by_name(candidate_name)
    return render_template('search.html', item=item)


@app.route('/skills/<skill_name>')
def search_by_skills_page(skill_name):
    item = get_by_skill(skill_name)
    return render_template('skill.html', item=item)


app.run()
