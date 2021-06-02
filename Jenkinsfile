pipeline {
  agent any
  stages {
    stage('Check for docker file') {
      steps {
        fileExists 'Dockerfile'
      }
    }

    stage('Build Image') {
      steps {
        sh '''git clone https://github.com/Patrick-Mutanho/test-jenkins.git
cd ./test-jenkins
'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''eval $(minikube docker-env)
docker build -t receive .

kubectl create deployment receive --image=receive'''
      }
    }

  }
}