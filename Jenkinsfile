pipeline {
    agent {
        any
    }
    stages {
        stage("Build") {
            steps{
                docker-compose -f local.yml build
            }
        }

        stage("Build") {
            steps{
                docker-compose -f local.yml run django pytest
            }
        }
    }
}