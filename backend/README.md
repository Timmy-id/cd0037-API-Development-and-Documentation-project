# Trivia API

## Introduction

Trivia API is an API that allows you to create questions, delete questions, search questions based on a particular category, view all available categories and play th game.

## Getting Started

BASE URL: [http://localhost:5000](http://localhost:5000)

## Errors

Example error takes this format:

```
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```

The response codes and messages are:

```
400 - bad request
404 - resource not found
405 - method not allowed
422 - unprocessable
500 - internal server error
```

## Resource Endpoint Library

### Questions Endpoint

```
GET /questions?page=pageNumber
```

This endpoint returns a list of questions, number of total questions and categories including pagination

#### Query Parameters

`page` optional for the first page

#### Sample Request

`curl http://localhost:5000/questions`

#### Responses

```
200
```

```
{
  {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
          }
      ],
    "success": true,
    "total_questions": 2
}
```

```
POST /questions
```

This endpoint creates a new question, which will require the question and answer text, category, and difficulty score.

#### Body

```
{
  "question": "Who is the president of Nigeria?",
  "answer": "General Mohammed Buhari",
  "category": 4,
  "difficulty": 3
}
```

#### Sample Request

`curl -X POST http://localhost:5000/questions -H 'Content-Type: application/json' -d '{"question":"Who is the president of Nigeria?","answer":"General Mohammed Buhari", "category": 4, "difficulty": 3}'`

#### Responses

```
200
```

```
{
  {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "General Mohammed Buhari",
            "category": 4,
            "difficulty": 3,
            "id": 5,
            "question": "Who is the president of Nigeria?"
          }
      ],
    "created": 5,
    "success": true,
    "total_questions": 2
}
```

```
POST /questions
```

This endpoint produces a result based on a search term.

#### Body

```
{
  "searchTerm": "actor"
}
```

#### Sample Request

`curl -X POST http://localhost:5000/questions -H 'Content-Type: application/json' -d '{"searchTerm": "actor"}'`

#### Responses

```
200
```

```
{
  "questions": [
      {
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4,
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      }
    ],
  "success": true,
  "total_questions": 1
}
```

```
DELETE /questions/{questionID}
```

This endpoint deletes a question using the question ID.

#### Body

Endpoint doesn't require body

#### Sample Request

`curl -X DELETE http://localhost:5000/questions/5`

#### Responses

```
200
```

```
{
  "deleted": 5,
  "success": true
}
```

### Categories Endpoint

```
GET /categories
```

This endpoint returns all available categories

#### Query Parameters

This endpoint doesn't require a query parameter

#### Sample Request

`curl http://localhost:5000/categories`

#### Responses

```
200
```

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

```
POST /categories
```

This endpoint creates a new category.

#### Query Parameters

This endpoint doesn't require a query parameter

#### Body

```
{
  "type": "Education"
}
```

#### Sample Request

`curl -X POST http://localhost:5000/categories -H 'Content-Type: application/json' -d '{"type": "Education"}'`

#### Responses

```
200
```

```
{
    "category": {
        "id": 7,
        "type": "Education"
    },
    "success": true
}
```

```
GET /categories/{categoryID}/questions
```

This endpoint returns all the questions in a particular category

#### Query Parameters

This endpoint doesn't require a query parameter

#### Sample Request

`curl http://localhost:5000/categories/4/questions`

#### Responses

```
200
```

```
{
    "current_category": "History",
    "questions": [
        {
            "answer": "General Mohammed Buhari",
            "category": 4,
            "difficulty": 3,
            "id": 5,
            "question": "Who is the president of Nigeria?"
          }
    ],
    "success": true,
    "total_questions": 1
}
```

### Quiz Endpoint

```
POST /quizzes
```

This endpoint takes a category and previous question parameters and returns a random question within the given category if provided, and which is not one of the previous questions.

#### Query Parameters

This endpoint doesn't require a query parameter

#### Body

```
{
  "previous_questions": [],
  "quiz_category": 4
}
```

#### Sample Request

`curl -X POST http://localhost:5000/quizzes -H 'Content-Type: application/json' -d '{"previous_questions": [], "quiz_category": 4}'`

#### Responses

```
200
```

```
{
    "question": {
        "answer": "General Mohammed Buhari",
        "category": 4,
        "difficulty": 3,
        "id": 5,
        "question": "Who is the president of Nigeria?"
    },
    "success": true
}
```