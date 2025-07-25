pipeline {
  agent any

  stages {
    stage('Fetch Kafka Service Versions') {
      steps {
        script {
          // Define auth token and base URL as variables (for reusability and maintainability)
          def authToken = params.USER_ACCESS_TOKEN
          def solutionId = params.SolutionID
          def topicName = "cds-"+params.TopicName
          
          echo "The USER_ACCESS_TOKEN is : "+authToken
          
          def baseUrl = "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/"+solutionId

          echo "The Base URL is : "+baseUrl

                

          // Use shell commands to fetch and process data
          sh """
            curl -s -X GET \\
              -H "Authorization: Bearer ${authToken}" \\
              -H "Content-Length: 0" \\
              "${baseUrl}/services?env=design&type=kafka" | \\
            jq -r '[ .[] | { id: .id, serviceId: .serviceId } | select(.serviceId | startswith(${topicName})) ] | .[].id' | \\
            xargs -I {} curl -s -X DELETE \\
              -H "Authorization: Bearer ${authToken}" \\
              -H "Content-Length: 0" \\
              "${baseUrl}/services/{}"
          """
        }
      }
    }
  }
}
