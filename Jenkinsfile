pipeline {
    agent { docker 'python:3.6-alpine3.6'}
    stages {
        stage('Test') {
            steps {
                sh 'echo "Hello World"'
                sh 'python3 --version'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -la
                '''
            }
        }
    }
}
