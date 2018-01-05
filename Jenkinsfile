pipeline {
    agent {
        docker { image 'python:3.6-alpine3.6' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}
