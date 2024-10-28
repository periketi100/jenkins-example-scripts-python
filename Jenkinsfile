pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        cmd 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        cmd 'python3 hello.py'
      }
    }
  }
}
