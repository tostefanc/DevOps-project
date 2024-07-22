pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '21', daysToKeepStr: '5'))
    }
    stages {
        stage('build'){
            steps{
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