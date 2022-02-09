pipeline{
    agent{
        docker{
            image 'python:2-alpine'
        }
    }

    parameters {
        string(name: "num_1", defaultValue: "0", description:"Enter First Value")
        string(name: "num_2", defaultValue: "0", description:"Enter Second Value")
        choice(name: "operator", choices: ["add","substract","multiply"], description: "What operation do you want to perform?")
    }

    stages{
        stage("Checkout"){
            steps{
                checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'a47942f3-397b-4782-b472-4d1d9a28d682', url: 'https://github.com/Sachinkw/ci_cd_assign_repo.git']]]
            }
        }

        stage("UnitTest"){
            steps{
                git credentialsId: 'a47942f3-397b-4782-b472-4d1d9a28d682', url: 'https://github.com/Sachinkw/ci_cd_assign_repo.git'
                bat 'python sources/test.py'
            }
        }

        stage("Build"){
            steps{
                git credentialsId: 'a47942f3-397b-4782-b472-4d1d9a28d682', url: 'https://github.com/Sachinkw/ci_cd_assign_repo.git'
                bat 'python sources/main.py --x %num1% --y %num2% --o %operator%'
                
                // bat 'python -m py_compile sources/add2vals.py sources/c.py'
                // stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }


    post{
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }

}