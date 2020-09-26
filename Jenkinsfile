pipeline {
    agent {
        any
    }
    stages {
        stage("Build") {
            steps{
                sh "docker-compose -f local.yml build"
            }
        }

        stage("Build") {
            steps{
                sh "docker-compose -f local.yml run django pytest"
            }
        }
    }
}