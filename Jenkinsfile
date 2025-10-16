pipeline {
    agent any

    stages {    
        stage('Registering build artifact') {
            steps {
                echo 'Registering the metadata'
                echo 'Another echo to make the pipeline a bit more complex'
                registerBuildArtifactMetadata(
                    name: "test-artifact-demo",
                    version: "1.0.1",
                    type: "docker",
                    url: "http://non:1111",
                    digest: "6f637064707039346163663237383938",
                    label: "prod"
                )
            }
        }

        stage('Register Security Scan') {
            steps {
                script {
                    def anchoreFile = "${env.WORKSPACE}/anchore-findings.json"
                    echo "Anchore findings file path: ${anchoreFile}"
                    if (fileExists(anchoreFile)) {
                        echo "File exists, registering scan..."
                        registerSecurityScan(
                            artifacts: anchoreFile,
                            format: "JSON",
                            scanner: "Anchore"
                        )
                    } else {
                        error "anchore-findings.json not found!"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            // archiveArtifacts artifacts: 'trivy-results.sarif', fingerprint: true
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
