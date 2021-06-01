pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Check for docker file') {
      steps {
        fileExists 'Dockerfile'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''docker build -t receive .


'''
      }
    }

    stage('Deploy Container') {
      steps {
        sh '''
kubectl create -f receive '''
      }
    }

  }
}