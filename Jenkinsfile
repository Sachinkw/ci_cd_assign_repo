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
        stage("UnitTest"){
            steps{
                python sources/tests.py
            }
        }

        stage("Build"){
            steps{
                wget -q -O tests.py python https://github.com/Sachinkw/ci_cd_assign_repo/blob/master/sources/tests.py --x %num_1% --y %num_2% --o %operator%
                
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