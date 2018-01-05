pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.6-alpine3.6'
                }
            }
            steps {
                sh 'python3 --version'
            }
        }
    }
}
