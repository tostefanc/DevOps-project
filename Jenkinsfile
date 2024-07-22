pipeline {
    agent any
    triggers {
        pollSCM('H/1 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '21', daysToKeepStr: '5'))
    }
    stages {
        stage('checkout'){
            steps{
                git branch: 'second-part', url: 'https://github.com/tostefanc/DevOps-project.git'
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