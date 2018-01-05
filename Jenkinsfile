pipeline {
    agent { docker 'python:3.6.3',
            image 'node:7-alpine'
    }
    stages {
        stage('build') {
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
