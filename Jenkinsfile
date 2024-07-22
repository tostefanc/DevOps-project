pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '21', daysToKeepStr: '5'))
    }
    stages {
        stage('checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/tostefanc/DevOps-project.git'
                echo "build stage"
            }
        }
        stage('test'){
            steps{
                echo "test stage"
            }
        }
    }
    post {
        failure {
            echo "something failed"
        }
    }
}