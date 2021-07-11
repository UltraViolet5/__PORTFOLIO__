from psycopg2.extras import RealDictCursor
from psycopg2 import sql
import database_common

from os.path import join, dirname, realpath
import os

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images')


@database_common.connection_handler
def add_answer(cursor: RealDictCursor, answer):
    """
    Add answer.
    :param cursor: RealDictCursor
    :param answer: answer data -> dict
    :return: None
    """
    query = sql.SQL(
        """INSERT INTO answer (submission_time, vote_number, question_id, message, image, owner_id)
        VALUES  ((SELECT CURRENT_TIMESTAMP(0)), 0, %s, %s, %s, %s)"""
    )
    cursor.execute(query, (answer['question_id'], answer['message'], answer['image'], answer['owner_id']))


@database_common.connection_handler
def get_answers(cursor: RealDictCursor, question_id):
    """
    Read answers for specific question.
    :param cursor: RealDictCursor
    :param question_id: id question -> int, str
    :return: answers for specific question -> list
    """
    query = """
            SELECT * 
            FROM answer
            WHERE question_id = %(question_id)s
            ORDER BY submission_time DESC
            """
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_answer(cursor: RealDictCursor, answer_id):
    """
    Get specific answer.
    :param cursor: RealDictCursor
    :param answer_id: id answer -> int, str
    :return: answer -> list
    """
    query = f"""
            SELECT * 
            FROM answer
            WHERE id = %(answer_id)s
            """
    cursor.execute(query, {'answer_id': answer_id})
    return cursor.fetchone()


@database_common.connection_handler
def update_answer(cursor: RealDictCursor, answer_id, answer_message, answer_image):
    """
    Get specific answer.
    :param answer_image: new answer image
    :param answer_message: new message -> str
    :param cursor: RealDictCursor
    :param answer_id: id answer -> int, str
    :return: None
    """
    query = """
            UPDATE answer
            SET message = %s,
                image = %s
            WHERE id = %s
            """
    cursor.execute(query, (answer_message, answer_image, answer_id))


@database_common.connection_handler
def get_n_questions(cursor: RealDictCursor, n):
    """
    Get n number questions.
    :param n: number of questions -> int
    :param cursor: RealDictCursor
    :return: All questions -> list
    """
    query = """
            SELECT *
            FROM question 
            ORDER BY submission_time DESC 
            LIMIT %(n)s
            
            """
    cursor.execute(query, {'n': n})
    return cursor.fetchall()


@database_common.connection_handler
def get_questions(cursor: RealDictCursor, key, order, page=0, amount=6):
    """
    Get questions.
    :param order: "desc" or "asc" -> str
    :param key: value of param to sorting -> str
    :param cursor: RealDictCursor
    :return: All questions -> list
    """
    if order == "desc":
        query = sql.SQL("""
                SELECT *
                FROM question  
                ORDER BY {}
                LIMIT %s
                OFFSET %s;
                """).format(sql.Identifier(key))
    elif order == 'asc':
        query = sql.SQL("""
                    SELECT *
                    FROM question  
                    ORDER BY {} DESC
                    LIMIT %s
                    OFFSET %s;   
                     """).format(sql.Identifier(key))
    else:
        query = ""

    cursor.execute(query, (amount, page * amount))
    return cursor.fetchall()


@database_common.connection_handler
def get_question(cursor: RealDictCursor, question_id):
    """
    Get specific question.
    :param question_id: question id -> int, str
    :param cursor: RealDictCursor
    :return: All questions -> list
    """
    query = """
            SELECT *
            FROM question   
            WHERE id = %(question_id)s 
            """
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchone()


@database_common.connection_handler
def update_question(cursor: RealDictCursor, edited_question, question_id):
    """
    :param cursor:
    :param edited_question: RealDictRow
    :param question_id: int
    :return:  None
    """
    query = sql.SQL(""" UPDATE question 
                SET title = %s, 
                message = %s, 
                image = %s
                WHERE id = %s""")

    cursor.execute(query, (edited_question['title'], edited_question['message'], edited_question['image'], question_id))


@database_common.connection_handler
def add_question(cursor: RealDictCursor, question):
    """

    :param cursor:
    :param question:
    :return:
    """
    query = sql.SQL("""
            INSERT INTO question (submission_time, view_number, vote_number, title, message, image, owner_id)
            VALUES ((SELECT CURRENT_TIMESTAMP(0)), %s, %s, %s, %s, %s, %s) RETURNING id;
            """)
    cursor.execute(query, (0, 0, question['title'], question['message'], question['image'], question['owner_id']))
    return cursor.fetchone()


@database_common.connection_handler
def get_answer_comments(cursor: RealDictCursor, answer_id):
    """
    Get comments for specific answer.
    :param answer_id: answer id -> int, str
    :param cursor: RealDictCursor
    :return: comments for specific answer -> list
    """
    query = sql.SQL("""
            SELECT *
            FROM comment
            WHERE answer_id = %s
            ORDER BY submission_time DESC
            """)
    cursor.execute(query, answer_id)
    return cursor.fetchall()


@database_common.connection_handler
def get_question_comments(cursor: RealDictCursor, question_id):
    """
    Get comments for specific question.
    :param question_id: question id -> int, str
    :param cursor: RealDictCursor
    :return: comments for specific question -> list
    """
    query = sql.SQL("""
            SELECT *
            FROM comment
            WHERE question_id = %s
            ORDER BY submission_time DESC
            """)
    cursor.execute(query, question_id)
    return cursor.fetchall()


@database_common.connection_handler
def get_comment(cursor: RealDictCursor, comment_id):
    query = sql.SQL("""
            SELECT *
            FROM comment
            WHERE id = %s
            """)
    cursor.execute(query, comment_id)
    return cursor.fetchone()


@database_common.connection_handler
def add_comment(cursor: RealDictCursor, comment):
    query = sql.SQL("""
            INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count)
            VALUES ( NULL, %s, %s, (SELECT CURRENT_TIMESTAMP(0)), 0)
            """)
    cursor.execute(query, (comment['answer_id'], comment['message']))


@database_common.connection_handler
def edit_comment(cursor: RealDictCursor, comment):
    query = sql.SQL("""
             UPDATE comment 
             SET message = %s,
                 edited_count = edited_count + 1
             WHERE id = %s
             """)
    cursor.execute(query, (comment.get("message"), comment.get("comment_id")))


@database_common.connection_handler
def get_tags(cursor: RealDictCursor, question_id):
    """
    Get all tags by question id.
    :param question_id: question id -> int
    :param cursor: RealDictCursor
    :return: tags -> list
    """
    query = sql.SQL(""" SELECT id, name
                FROM tag
                LEFT JOIN question_tag
                on tag.id = question_tag.tag_id
                WHERE  question_id = %(question_id)s
            """)
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_tags_occurrences(cursor: RealDictCursor):
    """
    Get tags names, id and number of occurrence.
    :param cursor: RealDictCursor
    :return: tags -> list
    """
    query = """SELECT name, id, count(tag_id)
                FROM question_tag
                LEFT JOIN tag
                ON tag.id = public.question_tag.tag_id
                GROUP BY name, id
            """

    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_tag(cursor: RealDictCursor, key, order, tag_id):
    """
    Get all questions by tag.
    :param tag_id:
    :param order:
    :param key:
    :param cursor: RealDictCursor
    :return: questions -> list
    """
    if order == "desc":
        query = sql.SQL("""SELECT *
        FROM question
        LEFT JOIN question_tag
        ON question.id = question_tag.question_id
        WHERE tag_id = %(tag_id)s
        ORDER BY {}; 
                """).format(sql.Identifier(key))
    else:
        query = sql.SQL("""SELECT *
        FROM question
        LEFT JOIN question_tag
        ON question.id = question_tag.question_id
        WHERE tag_id = %(tag_id)s
        ORDER BY {} DESC;
                        """).format(sql.Identifier(key))
    cursor.execute(query, {'tag_id': tag_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_all_tags(cursor: RealDictCursor):
    """
    Get all tags.
    :param cursor: RealDictCursor
    :return: tags -> list
    """
    query = """SELECT *
    FROM tag"""

    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def add_tag_to_question(cursor: RealDictCursor, tag_id, question_id):
    """
    Add tag to question.
    :param cursor: RealDictCursor
    :param tag_id -> int
    :param question_id -> int
    :return: None
    """
    query = """INSERT INTO question_tag (question_id, tag_id)
        VALUES (%s, %s)"""

    cursor.execute(query, (question_id, tag_id))


@database_common.connection_handler
def create_new_tag(cursor: RealDictCursor, tag_name):
    """
    Add tag to question.
    :param cursor: RealDictCursor
    :param tag_name -> str
    :return: None
    """
    query = sql.SQL("""INSERT INTO tag (name) 
        VALUES (%(tag_name)s)""")

    cursor.execute(query, {'tag_name': tag_name})


@database_common.connection_handler
def get_tag_id(cursor: RealDictCursor, tag_name):
    query = sql.SQL("""SELECT id
    FROM tag
    WHERE name = (%(tag_name)s)""")

    cursor.execute(query, {'tag_name': tag_name})
    return cursor.fetchone()


@database_common.connection_handler
def increase_view_number(cursor: RealDictCursor, record_id, table_name):
    """
    Increase view number in specific question or answer.
    :param record_id: record id -> int, str
    :param table_name: name of data base ('answer' or 'question') -> str
    :param cursor: RealDictCursor
    :return: None
    """
    query = sql.SQL("""
            UPDATE {}
            SET view_number = view_number + 1
            WHERE id = %(record_id)s
            """).format(sql.Identifier(table_name), )
    cursor.execute(query, {'record_id': record_id})


@database_common.connection_handler
def like_or_dislike_record(cursor: RealDictCursor, record_id, table_name, mode):
    """
    Increase or decrease vote_number in specific data base.
    :param record_id: record id -> int, str
    :param table_name: data base name ('answer' or 'question') -> str
    :param mode: 'inc' - increase by 1, 'dec' - decrease by 1 -> str
    :param cursor: RealDictCursor
    :return: None
    """
    value = None
    if mode == 'inc':
        value = 1
    elif mode == 'dec':
        value = -1
    query = sql.SQL("""
            UPDATE {}
            SET vote_number = vote_number + %(value)s
            WHERE id = %(record_id)s
            """).format(sql.Identifier(table_name))
    cursor.execute(query, {'value': value, 'record_id': record_id})


@database_common.connection_handler
def remove_record(cursor: RealDictCursor, record_id, table_name):
    """
    Delete record with specific id.
    :param cursor: RealDictCursor
    :param record_id: record id -> int
    :param table_name: name od table -> str
    :return: None
    """
    query = sql.SQL("""
            DELETE FROM {}
            WHERE id = %(record_id)s
            """).format(sql.Identifier(table_name))
    cursor.execute(query, {'record_id': record_id})


def remove_comment(comment_id):
    """
    Remove comment.
    :param comment_id: comment id
    :return: None
    """
    remove_record(comment_id, 'comment')


@database_common.connection_handler
def remove_answer(cursor: RealDictCursor, answer_id):
    """
    Remove answer and comments belonging to the answer.
    :param cursor: RealDictCursor
    :param answer_id: answer id
    :return: None
    """
    query = sql.SQL("""
            DELETE FROM comment
            WHERE answer_id = %(answer_id)s
            """)
    cursor.execute(query, {'answer_id': answer_id})
    remove_record(answer_id, 'answer')


@database_common.connection_handler
def get_answer_ids_by_question_id(cursor: RealDictCursor, question_id):
    """
    Get answer id's from answers belonging to the question.
    :param cursor: RealDictCursor
    :param question_id: question id
    :return: list
    """
    query = sql.SQL("""
                SELECT id
                FROM answer
                WHERE question_id = %(question_id)s
                """)
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@database_common.connection_handler
def answer_accept(cursor: RealDictCursor, answer_id):
    """
    Accept answer.
    :param cursor: RealDictCursor
    :param answer_id: answer id -> int
    :return: None
    """
    query = sql.SQL("""
            UPDATE answer
            SET accepted = TRUE 
            WHERE id = %(answer_id)s
            """)
    cursor.execute(query, {'answer_id': answer_id})


@database_common.connection_handler
def answer_unaccept(cursor: RealDictCursor, answer_id):
    """
    Unaccept answer.
    :param cursor: RealDictCursor
    :param answer_id: answer id -> int
    :return: None
    """
    query = sql.SQL("""
            UPDATE answer
            SET accepted = FALSE 
            WHERE id = %(answer_id)s
            """)
    cursor.execute(query, {'answer_id': answer_id})


@database_common.connection_handler
def question_accept(cursor: RealDictCursor, question_id):
    """
    Accept question.
    :param cursor: RealDictCursor
    :param question_id: question id -> int
    :return: None
    """
    query = sql.SQL("""
            UPDATE question
            SET accepted = TRUE 
            WHERE id = %(question_id)s
            """)
    cursor.execute(query, {'question_id': question_id})


@database_common.connection_handler
def question_unaccept(cursor: RealDictCursor, question_id):
    """
    Unaccept question.
    :param cursor: RealDictCursor
    :param question_id: question id -> int
    :return: None
    """
    query = sql.SQL("""
            UPDATE question
            SET accepted = FALSE 
            WHERE id = %(question_id)s
            """)
    cursor.execute(query, {'question_id': question_id})


@database_common.connection_handler
def remove_question(cursor: RealDictCursor, question_id):
    """
    Remove question and answers belonging to the question.
    :param cursor: RealDictCursor
    :param question_id: question item -> str
    :return: None
    """
    answer_ids = get_answer_ids_by_question_id(question_id)

    # Remove comments for question answers
    for item in answer_ids:
        query1 = sql.SQL("""
                    DELETE FROM comment
                    WHERE answer_id = %(item_id)s
                    """)
        cursor.execute(query1, {'item_id': item['id']})

    # Remove answers for question
    query2 = sql.SQL("""
                DELETE FROM answer
                WHERE question_id = %(question_id)s
                """)
    cursor.execute(query2, {'question_id': question_id})

    # Remove tags from question
    query3 = sql.SQL("""
                DELETE FROM question_tag
                WHERE question_id = %(question_id)s 
                """)
    cursor.execute(query3, {'question_id': question_id})

    # Remove question
    remove_record(question_id, 'question')


def remove_file_from_question(question_id):
    """
    Remove file from specific question.
    :param question_id: question id -> int
    :return: None
    """
    answers = get_answers(question_id)

    for answer in answers:
        if answer['image'] is not None:
            filename = answer['image']
            filename_path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.exists(filename_path):
                os.remove(filename_path)
                print(f'Deleted {filename}')

    question = get_question(question_id)

    if question['image'] is not None:
        filename = question['image']
        filename_path = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.exists(filename_path):
            os.remove(filename_path)
            print(f'Deleted {filename}')


@database_common.connection_handler
def update_answer(cursor: RealDictCursor, answer_id, answer_message):
    """
    Update answer.
    :param cursor: RealDictCursor
    :param answer_id: answer id -> int
    :param answer_message: answer content -> str
    :return: None
    """
    query = sql.SQL("""
            UPDATE answer
            SET message = %(answer_message)s
            WHERE id = %(answer_id)s
            """)
    cursor.execute(query, {'answer_id': answer_id, 'answer_message': answer_message})


def remove_file_from_answer(answer_id):
    """
    Remove image attached to an answer.
    :param answer_id: answer id -> int
    :return: None
    """
    answer = get_answer(answer_id)
    if answer['image'] is not None:
        filename = answer['image']
        filename_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(filename_path):
            os.remove(filename_path)
            print(f'Deleted {filename}')


@database_common.connection_handler
def search_questions(cursor: RealDictCursor, s_phrase):
    """
    Search questions by search phrase.
    :param cursor: RealDictCursor
    :param s_phrase: search phrase -> str
    :return: search result -> list
    """
    query = """
            SELECT *
            FROM question
            WHERE LOWER(title) LIKE LOWER(%(search_key)s) 
            OR LOWER(message) LIKE LOWER(%(search_key)s)
            ORDER BY submission_time DESC
            """
    cursor.execute(query, {"search_key": ("%%" + s_phrase + "%%")})
    return cursor.fetchall()


@database_common.connection_handler
def search_answers(cursor: RealDictCursor, s_phrase):
    """
    Search answers by specific phrase.
    :param cursor: RealDictCursor
    :param s_phrase: search phrase -> str
    :return: search result -> list
    """
    query = """
            SELECT *
            FROM answer
            WHERE LOWER(message) LIKE LOWER(%(search_key)s)
            ORDER BY submission_time DESC
            """
    cursor.execute(query, {"search_key": ("%%" + s_phrase + "%%")})
    return cursor.fetchall()


@database_common.connection_handler
def remove_tag_from_question(cursor: RealDictCursor, question_id, tag_id):
    """
    Remove tag from question.
    :param cursor: RealDictCursor
    :param question_id: question id -> int
    :param tag_id: tag id -> int
    :return: None
    """
    query = sql.SQL("""
                DELETE FROM question_tag
                WHERE question_id = %s and tag_id = %s  
                """)
    cursor.execute(query, (question_id, tag_id))


@database_common.connection_handler
def add_user(cursor: RealDictCursor, user_data):
    """
    Add user.
    :param cursor: RealDictCursor
    :param user_data: user data -> list
    :return: None
    """
    query = sql.SQL("""INSERT INTO users (nick, email, pw_hash, birth_date,reputation, access_level, join_date)
        VALUES (%s, %s, %s, %s , %s, %s, CURRENT_DATE)""")

    cursor.execute(query, (
        user_data["nick"], user_data["email"], user_data["password"], user_data["birthday"], 0,
        user_data["access_level"]))


@database_common.connection_handler
def get_user(cursor: RealDictCursor, email):
    """
    Get user from date base.
    :param cursor: RealDictCursor
    :param email: email -> str
    :return: user date -> dict
    """
    query = sql.SQL("""
            SELECT * FROM users
            WHERE email = %(email)s
            LIMIT 1;
            """)

    cursor.execute(query, {'email': email})
    return cursor.fetchone()


@database_common.connection_handler
def get_record_count(cursor: RealDictCursor, user_id, table_name):
    """
    Get count of questions, answers or comments by user_id.
    :param cursor: RealDictCursor
    :param user_id: user id -> int
    :param table_name: table name -> str
    :return: Count of records with owner_id = user_id -> int
    """
    query = sql.SQL("""
                SELECT COUNT(owner_id)
                FROM {}
                WHERE owner_id = %(user_id)s
            """).format(sql.Identifier(table_name))

    cursor.execute(query, {'user_id': user_id})
    return cursor.fetchone().get('count')


@database_common.connection_handler
def get_count_of_table(cursor: RealDictCursor, table_name):
    """
    Get count of records in table.
    :param cursor: RealDictCursor
    :param table_name: name of data base table -> str
    :return: count of records -> dict {'count': n}
    """
    query = sql.SQL("""
            SELECT COUNT(*)
            FROM {}
            """).format(sql.Identifier(table_name))

    cursor.execute(query)
    return cursor.fetchone()


@database_common.connection_handler
def get_records_by_owner_id(cursor: RealDictCursor, owner_id, table_name):
    """
    Get specific records with table.owner_id = owner_id.
    :param table_name: table name -> str
    :param owner_id: owner id -> int
    :param cursor: RealDictCursor
    :return: All questions -> list
    """
    query = sql.SQL("""
            SELECT *
            FROM {}   
            WHERE owner_id = %(owner_id)s;
            """).format(sql.Identifier(table_name))

    cursor.execute(query, {'owner_id': owner_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_record(cursor: RealDictCursor, record_id, table_name):
    """
    Get specific question.
    :param table_name: table name -> str
    :param record_id: record id -> int
    :param cursor: RealDictCursor
    :return: All questions -> list
    """
    query = sql.SQL("""
            SELECT *
            FROM {}   
            WHERE id = %(record_id)s;
            """).format(sql.Identifier(table_name))
    cursor.execute(query, {'record_id': record_id})
    return cursor.fetchone()


@database_common.connection_handler
def get_top_rated_question(cursor: RealDictCursor):
    """
    Get top rated question.
    :param cursor: RealDictCursor
    :return: question content -> dict
    """
    query = """
            SELECT *
            FROM question
            WHERE vote_number = (SELECT MAX(vote_number) FROM question)
            """
    cursor.execute(query)
    return cursor.fetchone()


@database_common.connection_handler
def get_top_viewed_question(cursor: RealDictCursor):
    """
    Get top viewed question.
    :param cursor: RealDictCursor
    :return: question content -> dict
    """
    query = """
            SELECT *
            FROM question
            WHERE view_number = (SELECT MAX(view_number) FROM question)
            """
    cursor.execute(query)
    return cursor.fetchone()


@database_common.connection_handler
def get_top_rated_answer(cursor: RealDictCursor, question_id):
    """
    Get top rated answer.
    :param cursor: RealDictCursor
    :param question_id: question id -> int
    :return: answer content -> dict
    """
    query = sql.SQL("""
            SELECT *
            FROM (SELECT * FROM answer WHERE answer.question_id = %(question_id)s) qa
            WHERE vote_number = (SELECT MAX(question_answers.vote_number)
            FROM (SELECT * FROM answer WHERE answer.question_id = %(question_id)s) question_answers)
            """)
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchone()


@database_common.connection_handler
def get_users(cursor: RealDictCursor):
    """
    Get all users.
    :param cursor: RealDictCursor
    :return: users -> list
    """
    query = """
            SELECT *
            FROM users
            """

    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def reputation_question(cursor: RealDictCursor, question_id, points):
    """
    :param cursor: RealDictCursor
    :param question_id: question id -> int
    :param points: points -> int
    :return: None
    """
    query = f"""
            UPDATE users
            SET reputation = reputation + %s
            FROM question
            WHERE
                users.id = question.owner_id AND
                question.id = %s
            """
    cursor.execute(query, (points, question_id))


@database_common.connection_handler
def reputation_answer(cursor: RealDictCursor, answer_id, points):
    """
    :param cursor: RealDictCursor
    :param answer_id: -> int
    :param points: -> int
    :return: None
    """
    query = f"""
            UPDATE users
            SET reputation = reputation + %s
            FROM answer
            WHERE
                users.id = answer.owner_id AND
                answer.id = %s
            """
    cursor.execute(query, (points, answer_id))


@database_common.connection_handler
def is_question_liked_by_user(cursor: RealDictCursor, question_id, user_id):
    """
    Check if question is liked.
    :param cursor: RealDictCursor
    :param question_id: question id -> int
    :param user_id: user id -> int
    :return: bool
    """
    query = """
            SELECT * FROM activity
            WHERE owner_id = %s and question_id = %s
            """
    cursor.execute(query, (user_id, question_id))
    result = cursor.fetchone()
    if result is not None and result['liked']:
        return True
    else:
        return False


@database_common.connection_handler
def is_answer_liked_by_user(cursor: RealDictCursor, answer_id, user_id):
    """
    Check if question is liked.
    :param cursor: RealDictCursor
    :param answer_id: answer id -> int
    :param user_id: user id -> int
    :return: bool
    """
    query = """
            SELECT * FROM activity
            WHERE owner_id = %s and answer_id = %s
            """
    cursor.execute(query, (user_id, answer_id))
    result = cursor.fetchone()
    if result is not None and result['liked']:
        return True
    else:
        return False


@database_common.connection_handler
def save_user_question_likes(cursor: RealDictCursor, user_id, question_id):
    """
    Save user activity if user liked question.
    :param cursor: RealDictCursor
    :param user_id: user id -> int
    :param question_id: question id -> int
    :return: None
    """
    query_0 = """
            SELECT * FROM activity
            WHERE owner_id = %s AND question_id = %s
            """
    cursor.execute(query_0, (user_id, question_id))

    if cursor.fetchone() is not None:
        query_1 = """
            UPDATE activity
            SET liked = TRUE
            WHERE owner_id = %s and question_id = %s  
            """
        args = (user_id, question_id)
    else:
        query_1 = """
            INSERT INTO activity (owner_id, question_id, answer_id, comment_id, liked, date_time) 
            VALUES (%s, %s, %s, %s, True, (SELECT CURRENT_TIMESTAMP(0)))
            """
        args = (user_id, question_id, None, None)

    cursor.execute(query_1, args)


@database_common.connection_handler
def save_user_answer_likes(cursor: RealDictCursor, user_id, answer_id):
    """
    Save user activity if user liked answer.
    :param cursor: RealDictCursor
    :param user_id: user id -> int
    :param answer_id: answer id -> int
    :return: None
    """
    query_0 = """
            SELECT * FROM activity
            WHERE owner_id = %s AND answer_id = %s
            """

    cursor.execute(query_0, (user_id, answer_id))

    if cursor.fetchone() is not None:
        query_1 = """
            UPDATE activity
            SET liked = TRUE
            WHERE owner_id = %s and answer_id = %s  
            """
        args = (user_id, answer_id)
    else:
        query_1 = """
            INSERT INTO activity (owner_id, question_id, answer_id, comment_id, liked, date_time) 
            VALUES (%s, %s, %s, %s, True, (SELECT CURRENT_TIMESTAMP(0)))
            """
        args = (user_id, None, answer_id, None)

    cursor.execute(query_1, args)


@database_common.connection_handler
def undo_user_likes(cursor: RealDictCursor, user_id, question_id=None, answer_id=None, comment_id=None):
    """
    Undo user activity if user disliked question, answer or comment.
    Only one of param of (question_id, answer_id, comment_id) have to be not None. One record in table represent
    one activity for question or answer or comment.
    :param cursor: RealDictCursor
    :param user_id: user id -> int
    :param question_id: question id -> int
    :param answer_id: answer id  -> int
    :param comment_id: comment id -> int
    :return: None
    """
    query = """
            UPDATE activity
            SET liked = FALSE
            WHERE owner_id = %s            
            """

    if question_id is not None and answer_id is None and comment_id is None:
        query += "AND question_id = %s;"
        content_id = question_id
    elif answer_id is not None and comment_id is None and question_id is None:
        query += "AND answer_id = %s;"
        content_id = answer_id
    elif comment_id is not None and question_id is None and answer_id is None:
        query += "AND comment_id = %s;"
        content_id = comment_id
    else:
        raise AttributeError('Only one of arg (question_id, answer_id, comment_id) can be not None')
    cursor.execute(query, (user_id, content_id))
