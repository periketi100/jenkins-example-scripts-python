pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
        sh 'pip install "urllib3<2.0.0" "requests<2.31.0" --upgrade --force-reinstall'
        sh 'python3 -m pip install jq'
      }
    }
    stage('cds') {
      steps {
        sh 'python3 cds.py'
      }
    }
  }
}
