pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    tools {
        git 'Default'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '21', daysToKeepStr: '5'))
    }
    stages {
        stage('checkout') {
            steps {
                git branch: 'second-part', url: 'https://github.com/tostefanc/DevOps-project.git'
            }
        }
        stage('build'){
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('run backend servers') {
            steps {
                sh 'nohup python3 web_app.py &'
                sh 'nohup python3 rest_app.py &'
            }
        }
        stage('testing') {
            steps {
                sh 'python3 backend_testing.py'
                sh 'python3 frontend_testing.py'
                sh 'python3 combined_testing.py'
            }
        }
        stage('clean environment') {
            steps {
                sh 'python3 clean_environment.py'
            }
        }
    }
}