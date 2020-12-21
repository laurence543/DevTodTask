# DevTodTask
Heroku application (deployment link):
https://stormy-sea-28069.herokuapp.com/

## How to run:
1. Clone repo;
2. Connect to DB (PostgreSQL, sqlite3, etc.) with editing 'DevTodTask/settings.py' (DATABASES);
3. Migrate (python manage.py migrate)
4. Run server locally with 'venv + python manage.py runserver'

DB: Heroku PostgreSQL (AWS)
You can add a news post with InteractiveConsole (venv with django + 'python manage.py shell').
**Requirements** for connection to DB (psql):
- 'NAME',
- 'HOST',
- 'PORT': 5432,
- 'USER',
- 'PASSWORD'

**Essential Requirements** for developing project:
- Django==3.1.4
- djangorestframework==3.12.2
- gunicorn==20.0.4
- psycopg2==2.8.6

**Task Requirements:**
- [x] Code should be written with Python 3;
- [x] REST API should be Django and Django REST Framework based;
- [ ] API should be well documented with Postman collection. Make sure to use [Postman environments and variables](https://learning.postman.com/docs/postman/variables-and-environments/variables/#understanding-variables-and-environments), so you can switch between local API and deployed version;
- [ ] API has to run as a Docker container. API + Postgres should be launched with docker-compose;
- [ ] Code should be formatted with [Black](https://github.com/psf/black);
- [ ] Necessary to make sure that Flake8 linter passes. Would be great to have typing with [pyright](https://github.com/microsoft/pyright) as well;
- [x] The project should have clear README with steps to run it;
- [x] The code should be clean, passing linter checks and simple to understand;
- [x] Deploy API for testing to [Heroku](https://www.heroku.com/) or [DevSpace](https://devspace.cloud/);
