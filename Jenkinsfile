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

        stage('Run Unit Tests & Coverage') {
            steps {
                echo 'Running unit tests with coverage...'
                bat '''
                    if not exist reports mkdir reports
                    if not exist reports\html mkdir reports\html
                    "%PYTHON_PATH%" -m pip install --user -r requirements.txt
                    "%PYTHON_PATH%" -m pytest -v --junitxml=reports\junit.xml --cov=. --cov-report=xml:reports\coverage.xml --cov-report=html:reports\html --cov-report=term
                '''
                junit allowEmptyResults: false, testResults: 'reports/junit.xml'
                cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'reports/coverage.xml', failNoReports: true, failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 10, onlyStable: false, sourceEncoding: 'UTF_8'
                publishHTML(target: [
                    reportName: 'Coverage HTML',
                    reportDir: 'reports/html',
                    reportFiles: 'index.html',
                    keepAll: true, alwaysLinkToLastBuild: true, allowMissing: false
                ])
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Archiving artifacts...'
                archiveArtifacts artifacts: '*.py, Dockerfile, requirements.txt, reports/junit.xml, reports/coverage.xml', allowEmptyArchive: false
                archiveArtifacts artifacts: 'reports/html/**', allowEmptyArchive: false
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
