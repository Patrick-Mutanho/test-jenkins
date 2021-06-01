pipeline {
  agent none
  stages {
    stage('Check for docker file') {
      steps {
        fileExists 'Dockerfile'
      }
    }

    stage('Build Image') {
      steps {
        sh '''https://github.com/Patrick-Mutanho/test-jenkins.git
cd ./test-jenkins
'''
      }
    }

  }
}