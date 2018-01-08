pipeline {
    agent {
        docker {
            image 'python:3.6-alpine3.6'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo "Teddy ganteng!"'
                sh 'python3 manage.py test'
            }
        }
    }
}
