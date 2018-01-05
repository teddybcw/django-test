pipeline {
    agent { docker 'python:3.6-alpine3.6'}
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -la
                '''
            }
        }
    }
}
