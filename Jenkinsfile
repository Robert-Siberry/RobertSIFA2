pipeline {

    agent any

    stages {
        

        stage('Build Images') {

                steps {
                    
                    sh 'chmod +x ./scripts/*.sh'
                    sh './scripts/buildimages.sh'
                    
                }
            
        }     

         stage('Deploy Stack') {;fw

                 steps {

                     sh './scripts/deploystack.sh'


                }
        }

         stage('Clean'){

                 steps {

                     sh './scripts/clean.sh'
                    
                 }

        }

    }

}