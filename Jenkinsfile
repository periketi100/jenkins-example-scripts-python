pipeline {
  agent any

  stages {
    stage('Fetch Kafka Service Versions') {
      steps {
        script {
          // Define auth token and base URL as variables (for reusability and maintainability)
          def authToken = "MTQ5MmYzZTctZDYxZC00ZjVjLTgwMWMtNzk3OTgzMjRlNWZk"
          def baseUrl = "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/d0ny74319"

          // Use shell commands to fetch and process data
          sh """
            curl -s -X GET \\
              -H "Authorization: Bearer ${authToken}" \\
              -H "Content-Length: 0" \\
              "${baseUrl}/services?env=design&type=kafka" | \\
            jq -r '[ .[] | { id: .id, serviceId: .serviceId } | select(.serviceId | startswith("cds-")) ] | .[].id' | \\
            xargs -I {} curl -s -X GET \\
              -H "Authorization: Bearer ${authToken}" \\
              -H "Content-Length: 0" \\
              "${baseUrl}/services/{}"
          """
        }
      }
    }
  }
}
