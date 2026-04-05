pipeline {
    agent any

    stages {
        stage('Test Stage') {
            steps {
                echo 'Pipeline is working'
            }
        }

        stage('Clone Code') {
            steps {
                git 'https://github.com/uttamzure/Registration-Page-Student.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh 'nohup python3 app.py > app.log 2>&1 &'
            }
        }
    }
}