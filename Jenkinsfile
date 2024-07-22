pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('build'){
            echo "build stage"
        }
        stage('test'){
            echo "test stage"
        }
    }
    post {
        failure {
            echo "something failed"
        }
    }
}