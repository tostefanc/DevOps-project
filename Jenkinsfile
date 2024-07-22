pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
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
        stage('run backend servers') {
            steps {
                sh 'nohup python web_app.py &'
                sh 'nohup python rest_app.py &'
            }
        }
        stage('testing') {
            steps {
                sh 'python backend_testing.py'
                sh 'python frontend_testing.py'
                sh 'python combined_testing.py'
            }
        }
        stage('clean environment') {
            steps {
                sh 'python clean_environment.py'
            }
        }
    }
}