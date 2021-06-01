pipeline {
  agent {
    node {
      label 'main'
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
        sh '''#! /bin/bash.

eval $(minikube docker-env)

docker build -t receive .


'''
      }
    }

    stage('Deploy Container') {
      steps {
        sh '''#!/bin/sh

kubectl create -f receive '''
      }
    }

  }
}