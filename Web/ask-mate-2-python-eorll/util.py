from flask import make_response, render_template, session
from psycopg2.extras import RealDictCursor

import re
import database_common
import data_manager

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def cut_question_in_questions(questions: list, number_of_word: int):
    """

    :param questions: list of list
    :param number_of_word:
    :return: list of list with shorten question (index [5] from csv)
    """

    for question in questions:
        split_message = question[5].split(" ", number_of_word)
        split_message.pop(len(split_message) - 1)
        question[5] = " ".join(split_message) + "..."

    return questions


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@database_common.connection_handler
def get_next_id(cursor: RealDictCursor, data_table):
    """
    Get next id for specific data base
    :param cursor: RealDictCursor
    :param data_table: data table name -> str
    :return: id -> int
    """
    query = """                
                SELECT count(*)
                FROM %s
                """ % data_table
    cursor.execute(query)
    tab_count = cursor.fetchall()
    return tab_count[0]['count'] + 1


def get_default_question():
    return {
            'view_number': 0,
            'vote_number': 0,
            'title': 'Provide title...',
            'Message': 'Provide message',
            'image': ''
            }


def get_count_of_answers(question_id):
    answers = data_manager.get_answers(question_id)
    return len(answers)


def add_all_tags(question_id, tags_id):
    # Add all existing tags to question

    for tag_id in tags_id:
        if tag_id != 'new_tag':
            data_manager.add_tag_to_question(tag_id=int(tag_id), question_id=int(question_id))


def create_new_tag(tags_id, question_id):
    # Create and add new tag to question.
    if tags_id['new_tag'] != '' and not check_if_tag_exist(tag_name=tags_id['new_tag']):
        new_tag = (tags_id['new_tag']).lower()
        data_manager.create_new_tag(tag_name=new_tag)
        new_tag_id = data_manager.get_tag_id(tag_name=new_tag)
        data_manager.add_tag_to_question(tag_id=int(new_tag_id['id']), question_id=int(question_id))


def check_if_tag_exist(tag_name):
    """
    :param tag_name -> str (tag name to check)
    :return: True - exist
            False - don't exist
    """

    all_tags = data_manager.get_all_tags()

    for tag in all_tags:
        if tag['name'] == tag_name:
            return True
    return False


def mark_search_phrase(word: str, phrase: str):
    """
    Mark in phrase a specific word by html markup.
    :param word: str
    :param phrase: str
    :return: phrase with markups -> str
    """
    html_span_before = '<span class="badge rounded-pill bg-success">'
    html_span_after = '</span>'
    re_query = build_re(word)
    return re.sub('(' + f"{re_query}" + ")", html_span_before + r"\1" + html_span_after, phrase)


def build_re(word: str):
    """
    Build re query for word with case sensitivity.
    :param word: str
    :return: re query -> str
    """
    result = ''
    for letter in word:
        result += '[' + letter.lower() + letter.upper() + ']'
    return result


def get_response():
    five_questions = data_manager.get_n_questions(4)
    resp = make_response(render_template('index.html',
                                         questions=five_questions,
                                         get_count_of_answers=get_count_of_answers))

    resp.set_cookie('logged', str(session['logged']))
    resp.set_cookie('user_id', str(session['user_id']))
    resp.set_cookie('user_nick', str(session['user_nick']))
    return resp
