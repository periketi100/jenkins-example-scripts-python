pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'curl -s -X GET -H "Authorization: Bearer MTQ5MmYzZTctZDYxZC00ZjVjLTgwMWMtNzk3OTgzMjRlNWZk" -H "Content-Length: 0"  "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/d0ny74319/services?env=design&type=kafka" | jq -r '[ .[] | { id: .id, serviceId: .serviceId} | select(.serviceId | startswith("cds-"))] | .[].id' | xargs -I {} curl GET -H "Authorization: Bearer MTQ5MmYzZTctZDYxZC00ZjVjLTgwMWMtNzk3OTgzMjRlNWZk" -H "Content-Length: 0"  "https://console.dms.ort.usw2.ficoanalyticcloud.com/com.fico.dmp.manager/rest/dmp/runtime/solutions/d0ny74319/services/"{}'
      }
    }
}
}
