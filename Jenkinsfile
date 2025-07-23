pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install requests'
        sh 'pip3 install jq'
      }
    }
    stage('cds') {
      steps {
        sh 'python cds.py'
      }
    }
  }
}
