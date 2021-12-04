1) In project folder create venv:
   Command (from bash):
   - cd name_project_folder/
   - python -m venv venv
   
2) Activate your Virtual environment:
   Command (from bash):
   - source venv/Scripts/activate

3) Install all requirements from file requiremnts.txt:
   - pip install -r /path/to/requirements.txt

4) Run the command to create the initial database:
   - python manage.py makemigrations
   - python manage.py migrate

5) Create a couple of users and groups.


REST API links:
Link for see all users:
- http://127.0.0.1:8000/api/users/
Link for retrieve, update or delete a USERS instance (insert pk of user):
- http://127.0.0.1:8000/api/users/<pk>
Link for see all groups:
- http://127.0.0.1:8000/api/groups/
Link for retrieve, update or delete a GROUPS instance (insert pk of group):
- http://127.0.0.1:8000/api/groups/<pk>