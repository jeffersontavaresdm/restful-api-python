# PYTHON-FLASK RESTFUL API

A simple RESTful API using Python and Flask to practice and improve knowledge

### install
```
pip install -r requirements.txt
```

### up a docker container with a postgresql database
```
docker compose -f docker/docker-compose.yml up -d
```

### run
```
python app.py
```

### all routes
- health of server (GET): `http://127.0.0.1:5000/health`
- list users (GET): `http://127.0.0.1:5000/users`
- create user (POST): `http://127.0.0.1:5000/users`
- update user (PUT): `http://127.0.0.1:5000/users/{user_id}`
- delete user (DELETE): `http://127.0.0.1:5000/users/{user_id}`

#

<br>

<div align="center">
  <a  href="https://github.com/jeffersontavaresdm">
    <img width="30%" src="https://github.com/jeffersontavaresdm/jeffersontavaresdm/blob/main/images/rs.gif" width="25"/>
  </a>
</div>
