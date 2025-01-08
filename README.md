# smart-nonsense-exam

# Setup:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Running server
`python manage.py runserver`

## Add Tags data
1. Go to `http://localhost:8000/admin` to login using the superuser account  
2. Go to `http://localhost:8000/admin/app/tag/add/` to add a Tag category

## Setup Postman APIs
1. Using postman, import the `Local.postman_environment.json` environment file and `Smart Nonsense.postman_collection.json` API file
2. Replace the `username` and `password` fields with your user account


# Documentation
Once you've setup the postman APIs, you can see all the API endpoints.

## Questions API
* POST /questions/
  * Creates a question
* GET /questions/
  * Get list of questions
  * Can filter by Question, Solution or tag name
* GET /questions/{id}/
  * Get question by id
* PATCH /questions/{id}/
  * Update a question
* DELETE /questions/{id}/
  * Delete a question

## Structured JSON for Unity API
* GET /unity/questions/{id}/
  * Get question by id

## Sample display on HTML
* GET /display/{id}/
  * Get question by id

