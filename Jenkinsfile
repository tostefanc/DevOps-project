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
                git branch: 'second-part', url: 'https://github.com/tostefanc/DevOps-project.git', credentialsId: 'a27a360c-fa85-4b12-9056-4cac5f8bd076'            }
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
    post {
        failure {
             echo 'This will run only if Pipeline Failed'
             mail bcc: '', body: "<b>DevOps Project JOB:</b>: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> Build URL: ${env.BUILD_URL}", charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: credentialsId: '11bd0291-558c-4934-99bc-04475cb282b2';
         }
    }
}