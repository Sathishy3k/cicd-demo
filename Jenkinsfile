pipeline {
    agent {
        label 'wsl'
    }

    tools {
        git 'git-linux'
    }

    environment {
        DOCKER_IMAGE = 'cicd-demo-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
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
                sh '''
                    set -e
                    docker build -t "$DOCKER_IMAGE:$DOCKER_TAG" .
                    docker tag "$DOCKER_IMAGE:$DOCKER_TAG" "$DOCKER_IMAGE:latest"
                '''
            }
        }

        stage('Build Python') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    set -e
                    PY=$(command -v python3 || command -v python)
                    "$PY" -m pip install --user -r requirements.txt
                '''
            }
        }

        stage('Run Python Program') {
            steps {
                echo 'Running the Python application...'
                sh '''
                    set -e
                    PY=$(command -v python3 || command -v python)
                    "$PY" app.py
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    set -e
                    PY=$(command -v python3 || command -v python)
                    "$PY" -m unittest test_app.py -v
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
            sh '''
                set +e
                docker rmi "$DOCKER_IMAGE:$DOCKER_TAG" || true
            '''
        }
    }
}
