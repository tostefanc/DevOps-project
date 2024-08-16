### DevOps Project
Example of db_secrets.py 
```python
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_SCHEMA = 'mydb'
DB_PORT = 3306
DB_HOST = '127.0.0.1'
```

For the Jenkins email notification:
- the right configuration needs to be done under the E-mail Notification section from Manage Jenkins/System
- a secret text credential needs to be created in Jenkins with ID: notification-email-address and must contain the email address to receive the alerts