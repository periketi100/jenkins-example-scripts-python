pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('cds') {
      steps {
        sh 'python3 cds.py'
      }
    }
  }
}
