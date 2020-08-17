pipeline {

    agent any

    stages {
        

        stage('Build Images') {

                steps {
                    
                    sh 'chmod +x ./scripts/*.sh'
                    sh './scripts/buildimages.sh'
                    
                }
            
            }     

        stage('Deploy Stack') {

                steps {
                       
                    sh 'chmod +x ./scripts2/*.sh'
                    sh './scripts2/deploy_stack.sh'

                }
            }

        stage('Clean'){

                steps {

                    sh 'chmod +x ./scripts/*.sh'
                    sh './scripts/clean.sh'
                    
                }

            }

    }

}