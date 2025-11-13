pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'cicd-demo-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        PYTHON_PATH = 'C:\\Users\\SPeriyasamy\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'

    }

    stages {
        stage('Get Code') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }

        stage('Build Container') {
            steps {
                echo 'Building Docker container...'
                /*
                bat '''
                    docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% .
                    docker tag %DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_IMAGE%:latest
                '''
                */

            }
        }

        stage('Build Python') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                    "%PYTHON_PATH%" -m pip install --user -r requirements.txt
                '''
            }
        }

        stage('Run Python Program') {
            steps {
                echo 'Running the Python application...'
                bat '"%PYTHON_PATH%" app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    "%PYTHON_PATH%" -m unittest test_app.py -v
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Archiving artifacts...'
                archiveArtifacts artifacts: '*.py, Dockerfile, requirements.txt', allowEmptyArchive: false
                echo 'Artifacts archived successfully!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
        always {
            echo 'Cleaning up...'
            /*
            bat '''
                docker rmi %DOCKER_IMAGE%:%DOCKER_TAG% || exit /b 0
            '''
            */
        }
    }
}
