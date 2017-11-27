#!groovy


node ("raspberry") {

   

    properties([

        buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '2', numToKeepStr: '6'))//,

    ])


    stage('Install'){

        sh("pip install -r requirements.txt")

    }


        


    stage('Run') {
        timeout(time: 30, unit: 'SECONDS') {
            sh('python laser_pi.py')
        }
    }

    
}




