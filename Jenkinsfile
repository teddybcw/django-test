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
                sh 'pip3 install django'
                sh 'echo "Teddy ganteng!"'
                sh 'python3 manage.py test'
            }
        }
        stage('testing') {
            post {
                always {
                    sh 'python3 manage.py test'
                }
            }
        }
    }
}
