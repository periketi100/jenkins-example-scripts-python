pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install requests'
      }
    }
    stage('cds') {
      steps {
        sh 'python3 cds.py'
      }
    }
  }
}
