from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from sqlalchemy.sql.functions import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.route('/categories')
    def get_all_categories():
        """
        It queries the database for all categories, orders them by id, and returns a json object with
        the categories
        :return: A list of all the categories in the database.
        """
        categories = Category.query.order_by(Category.id).all()
        formatted_categories = {
            category.id: category.type for category in categories}

        return jsonify({
            "success": True,
            "categories": formatted_categories
        })

    @app.route('/questions')
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        categories = get_all_categories().get_json()["categories"]
        current_questions = paginate_questions(request, selection)

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'categories': categories,
            'current_category': ''
        })

    @ app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_questions(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                abort(404)
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                "success": True,
                "deleted": question_id
            })
        except Exception:
            abort(422)

    @ app.route('/questions', methods=['POST'])
    def create_questions():
        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty_score = body.get('difficulty', None)
        search = body.get('searchTerm', None)

        try:
            if search:
                selection = Question.query.filter(
                    Question.question.ilike(f'%{search}%')).order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(selection)
                })
            else:
                question = Question(question=new_question, answer=new_answer,
                                    category=new_category, difficulty=new_difficulty_score)
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                return jsonify({
                    "success": True,
                    "created": question.id,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all())
                })
        except Exception:
            abort(422)

    @app.route('/categories', methods=['POST'])
    def create_category():
        body = request.get_json()

        new_category = body.get('type', None)

        if not new_category:
            abort(400)

        try:
            category = Category(new_category)
            db.session.add(category)
            db.session.commit()
            formatted_response = category.format()

            return jsonify({
                "success": True,
                "category": formatted_response
            })
        except Exception:
            abort(400)

    @ app.route('/categories/<int:category_id>/questions')
    def get_questions_per_category(category_id):
        try:
            if not category_id:
                abort(404)
            questions = Question.query.filter(
                Question.category == category_id).all()
            category = Category.query.get(category_id)
            current_questions = paginate_questions(request, questions)

            return jsonify({
                "success": True,
                "questions": current_questions,
                "total_questions": len(questions),
                "current_category": category.type
            })
        except Exception:
            abort(404)

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        """
        It takes in a request from the frontend, checks if the request has a quiz_category and
        previous_questions, if it does, it checks if the quiz_category is not None, if it is not None,
        it queries the database for questions that match the quiz_category and are not in the
        previous_questions list, if the quiz_category is None, it queries the database for questions
        that are not in the previous_questions list, if the length of the questions list is greater than
        0, it chooses a random question from the list and returns it, if the length of the questions
        list is 0, it returns None
        :return: A question object
        """
        request_data = request.get_json()

        quiz_category = None
        previous_questions = None

        if request_data:
            quiz_category = request_data["quiz_category"]
            previous_questions = request_data["previous_questions"]

            if quiz_category:
                questions = Question.query.filter_by(category=quiz_category).filter(
                    ~Question.id.in_(previous_questions)).order_by(random()).all()
            else:
                questions = Question.query.filter(
                    ~Question.id.in_(previous_questions)).order_by(random()).all()
            if len(questions) > 0:
                for single_question in questions:
                    question = single_question.format()
            else:
                question = None
            return jsonify({
                "success": True,
                "question": question
            })
        else:
            abort(400)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(405)
    def wrong_request(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    return app
