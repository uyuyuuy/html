pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/uyuyuuy/html.git']]])                
                script {
                    build_tag = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                }
                echo "build_tag: ${build_tag}"
                echo 'Clone Success'
            }
        }
        
        stage('Build') {
            steps {
                // sh "docker build -t harbor.mydong.vip/xiangdong/ ." 
                //docker push 
                echo 'Build Success'
            }
        }
        
        // stage('Deployment') {
        //     steps {
        //         sh 'sed "s///g" deploymnet.yaml'
        //         kubectl apply -f deployment.yaml
        //     }
        // }
        
        stage('Clear') {
            steps {
                cleanWs()
            }
            
        }
    }
}
