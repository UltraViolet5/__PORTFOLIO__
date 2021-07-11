import math

import bcrypt
from flask import Flask, render_template, request, redirect, url_for, flash, Markup, session
import data_manager
import util
import os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.secret_key = 'sekretny klucz'

# Add my func to jinja env
app.jinja_env.globals.update(get_all_tags=data_manager.get_tags_occurrences,
                             get_tags=data_manager.get_tags,
                             session=session,
                             get_record_count=data_manager.get_record_count,
                             get_count_of_answers=util.get_count_of_answers,
                             get_question=data_manager.get_question,
                             get_answer=data_manager.get_answer,
                             get_user=data_manager.get_record,
                             get_n_questions=data_manager.get_n_questions,
                             get_top_rated_question=data_manager.get_top_rated_question,
                             get_top_viewed_question=data_manager.get_top_viewed_question,
                             get_top_rated_answer=data_manager.get_top_rated_answer,
                             is_question_liked_by_user=data_manager.is_question_liked_by_user,
                             is_answer_liked_by_user=data_manager.is_answer_liked_by_user,
                             get_count_of_table=data_manager.get_count_of_table,
                             round_up=math.ceil,
                             int=int)


@app.route("/")
def index():
    questions = data_manager.get_n_questions(4)
    top_rated_question = data_manager.get_top_rated_question()
    top_viewed_question = data_manager.get_top_viewed_question()

    return render_template('index.html')


@app.route("/question/<question_id>")
def display_question(question_id):
    data_manager.increase_view_number(question_id, 'question')
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers(question_id)
    answers_count = len(answers)

    return render_template("question.html", question=question, answers=answers,
                           get_comments=data_manager.get_answer_comments,
                           answers_count=answers_count)


# TODO reimplement vote
@app.route("/question/<question_id>/vote")
def vote(question_id):
    # data_manager.increase_vote_number(question_id, 'question.csv')

    return redirect(url_for('display_question', question_id=question_id, voted=True))


@app.route("/question/<question_id>", methods=['POST'])
def edit_question(question_id):
    edited_question = dict(request.form)
    if edited_question['image_option'] == 'change':
        data_manager.remove_file_from_question(question_id)
        edited_question['image'] = upload_image()
    elif edited_question['image_option'] == 'remove':
        data_manager.remove_file_from_question(question_id)
        edited_question['image'] = None
    else:
        edited_question['image'] = data_manager.get_question(question_id)['image']

    data_manager.update_question(edited_question, question_id)
    return redirect(url_for('display_question', question_id=question_id))


@app.route("/question/<question_id>/edit-page")
def edit_question_form(question_id):
    question = data_manager.get_question(question_id)

    return render_template('question_form.html', question=question, mode='edit')


@app.route("/comment/add", methods=["POST"])
def add_comment():
    comment = dict(request.form)
    comment['owner_id'] = session['user_id']

    data_manager.add_comment(comment)
    return redirect(url_for('display_question', question_id=comment['question_id']))


@app.route("/comment/<question_id>/<answer_id>/add")
def add_comment_form(question_id, answer_id):
    answer = data_manager.get_answer(answer_id)
    return render_template('comment_form.html', answer_id=answer_id, question_id=question_id, answer=answer)


@app.route("/comment/<question_id>/<answer_id>/<comment_id>/edit")
def edit_comment_form(question_id, answer_id, comment_id):
    answer = data_manager.get_answer(answer_id)
    comment = data_manager.get_comment(comment_id)
    comment_msg = comment.get("message")
    comment_id = comment.get("id")
    print(comment_msg)
    return render_template('edit_comment.html', answer_id=answer_id, question_id=question_id, comment_msg=comment_msg,
                           answer=answer, comment_id=comment_id, comment=comment)


@app.route("/comment/edit", methods=["POST"])
def edit_comment():
    comment = dict(request.form)
    data_manager.edit_comment(comment)
    return redirect(url_for('display_question', question_id=comment['question_id']))


@app.route("/answer/<question_id>/<answer_id>/edit")
def edit_answer_form(question_id, answer_id):
    question = data_manager.get_question(question_id)
    answer = data_manager.get_answer(answer_id)
    tags = data_manager.get_tags(question_id)
    answer_msg = answer.get("message")
    answers_count = util.get_count_of_answers(question_id)

    return render_template('edit_answer.html', answer_id=answer_id, answer=answer, amsg=answer_msg,
                           question_id=question_id, question=question, tags=tags, answers_count=answers_count)


@app.route("/answer/<answer_id>/<question_id>/edit", methods=['POST'])
def edit_answer(answer_id, question_id):
    upd_answer = dict(request.form)
    upd_answer['image'] = upload_image()
    data_manager.update_answer(answer_id, upd_answer['message'])

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/list/<page>')
def list_questions(page):
    key = request.args.get('key', default="submission_time", type=str)
    order = request.args.get('order', default='asc', type=str)
    questions = data_manager.get_questions(key, order, page=int(page))

    return render_template("list_question.html",
                           questions=questions,
                           order=order,
                           get_count_of_answers=util.get_count_of_answers,
                           key=key,
                           current_page=int(page))


@app.route("/add-question")
def add_question_form():
    default_question = util.get_default_question()

    # mode below can be 'add' or 'edit'
    return render_template('question_form.html', mode='add', question=default_question)


@app.route("/question", methods=['POST'])
def add_question():
    new_question = dict(request.form)
    new_question['image'] = upload_image()
    new_question['owner_id'] = session['user_id']

    question_id = data_manager.add_question(new_question)['id']
    return redirect(url_for('display_question', question_id=question_id))


@app.route('/', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            return None
        image = request.files['image']
        # if user does not select file, browser also
        # submit an empty part without filename
        if image.filename == '':
            return None
        if image and util.allowed_file(image.filename):
            filename = secure_filename(image.filename)
            while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)) or filename == '':
                filename = '1' + filename

            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return filename


@app.route('/question/<question_id>/<user_id>/like-it', methods=['GET', 'POST'])
def like_question(question_id, user_id):
    data_manager.like_or_dislike_record(question_id, 'question', mode='inc')
    data_manager.reputation_question(question_id=question_id, points=5)
    data_manager.save_user_question_likes(user_id, question_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/<user_id>/dislike-it', methods=['GET', 'POST'])
def dislike_question(question_id, user_id):
    data_manager.like_or_dislike_record(question_id, 'question', mode='dec')
    data_manager.undo_user_likes(user_id, question_id=question_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/answer/<answer_id>/<question_id>/<user_id>/like-it', methods=['GET', 'POST'])
def like_answer(answer_id, question_id, user_id):
    data_manager.like_or_dislike_record(answer_id, 'answer', mode='inc')
    data_manager.save_user_answer_likes(user_id, answer_id)
    data_manager.reputation_answer(answer_id=answer_id, points=10)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/answer/<answer_id>/<user_id>/<question_id>/dislike-it', methods=['GET', 'POST'])
def dislike_answer(answer_id, user_id, question_id):
    data_manager.like_or_dislike_record(answer_id, 'answer', mode='dec')
    data_manager.undo_user_likes(user_id, answer_id=answer_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route("/answer/<question_id>/add")
def add_answer_form(question_id):
    question = data_manager.get_question(question_id)
    return render_template('add_answer.html', question=question)


@app.route("/answer/<question_id>/add", methods=['POST'])
def add_answer(question_id):
    new_answer = dict(request.form)
    new_answer['image'] = upload_image()
    new_answer['owner_id'] = session['user_id']
    new_answer['question_id'] = question_id

    data_manager.add_answer(new_answer)
    return redirect(url_for('display_question', question_id=question_id))


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    data_manager.remove_file_from_question(question_id)
    data_manager.remove_question(question_id)

    return redirect(url_for("list_questions", page=0))


@app.route("/answer/<question_id>/<answer_id>/delete")
def delete_answer(question_id, answer_id):
    data_manager.remove_file_from_answer(answer_id)
    data_manager.remove_answer(answer_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/comment/<comment_id>/<question_id>/delete')
def delete_comment(comment_id, question_id):
    data_manager.remove_comment(comment_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route('/list-by-tag/<tag_id>')
def list_questions_by_tag(tag_id):
    key = request.args.get('key', default="submission_time", type=str)
    order = request.args.get('order', default='asc', type=str)
    questions = data_manager.get_questions_by_tag(key, order, tag_id)

    return render_template("list_question.html",
                           questions=questions,
                           order=order,
                           tag_id=tag_id,
                           key=key)


@app.route('/question/<question_id>/new-tag')
def tag_form(question_id):
    question = data_manager.get_question(question_id)
    question_tags = data_manager.get_tags(question_id)
    all_tags = data_manager.get_all_tags()

    return render_template("tag_form.html", question=question,
                           question_tags=question_tags,
                           all_tags=all_tags,
                           question_id=question_id,
                           tag_editing=True)


@app.route('/question/<question_id>/new-tag', methods=['POST'])
def add_tag(question_id):
    new_tags = dict(request.form)
    util.add_all_tags(question_id=question_id, tags_id=new_tags)
    util.create_new_tag(question_id=question_id, tags_id=new_tags)
    return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/tag/<tag_id>/delete')
def delete_tag(question_id, tag_id):
    data_manager.remove_tag_from_question(question_id=question_id, tag_id=tag_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.errorhandler(404)
def missing_page(e):
    return render_template('missing_page.html')


@app.errorhandler(500)
def server_error(e):
    return render_template('server_error.html')


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route("/search?g", methods=["POST", "GET"])
def search():
    search_phrase = dict(request.form)['search_phrase']
    questions = data_manager.search_questions(search_phrase)
    answers = data_manager.search_answers(search_phrase)

    return render_template('search-results.html',
                           questions=questions,
                           answers=answers,
                           search_phrase=search_phrase,
                           get_count_of_answers=util.get_count_of_answers,
                           mark_searched_word=util.mark_search_phrase,
                           Markup=Markup)


@app.route("/registration/register", methods=["POST"])
def register():
    register_data = dict(request.form)

    if register_data.get("password") == register_data.get("repeat_password"):
        salt = bcrypt.gensalt()
        pw_hash = bcrypt.hashpw(register_data.get("password").encode('utf-8'), salt)
        register_data['password'] = pw_hash.decode('utf-8')

        data_manager.add_user(register_data)
        return redirect(url_for("index"))


@app.route('/login', methods=['POST', 'GET'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_data = data_manager.get_user(email)
    session['logged'] = False
    session['user_nick'] = None
    session['user_id'] = None
    session['access'] = None

    if user_data and bcrypt.checkpw(password.encode('UTF-8'), user_data['pw_hash'].encode('UTF-8')):
        session['logged'] = True
        session['user_nick'] = user_data['nick']
        session['user_id'] = user_data['id']
        session['access'] = user_data['access_level']

    return render_template('index.html')


@app.route('/logout')
def logout():
    session['logged'] = False
    session['user_nick'] = None
    session['user_id'] = None
    session['access'] = None

    return render_template('index.html')


@app.route('/user/<user_id>')
def user(user_id):
    user_data = data_manager.get_record(user_id, 'users')
    questions = data_manager.get_records_by_owner_id(user_id, 'question')
    answers = data_manager.get_records_by_owner_id(user_id, 'answer')
    comments = data_manager.get_records_by_owner_id(user_id, 'comment')

    return render_template('user.html', user=user_data,
                           questions=questions,
                           answers=answers,
                           comments=comments)


@app.route('/users')
def users():
    users_data = data_manager.get_users()

    return render_template('users.html', users=users_data)


@app.route("/answer/<question_id>/<answer_id>/accept")
def accept_answer(question_id, answer_id):
    # FIXME check if session user_id is correct
    # FIXME implementation transaction -> BEGIN; ... COMMIT;
    data_manager.answer_accept(answer_id)
    data_manager.reputation_answer(answer_id=answer_id, points=15)

    return redirect(url_for('display_question', question_id=question_id))


@app.route("/answer/<question_id>/<answer_id>/unaccept")
def unaccept_answer(question_id, answer_id):
    data_manager.answer_unaccept(answer_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route("/question/<question_id>/accept")
def accept_question(question_id):
    data_manager.question_accept(question_id)

    return redirect(url_for('display_question', question_id=question_id))


@app.route("/question/<question_id>/unaccept")
def unaccept_question(question_id):
    data_manager.question_unaccept(question_id)

    return redirect(url_for('display_question', question_id=question_id))


if __name__ == "__main__":
    app.run()
