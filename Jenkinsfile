pipeline{
    agent none

    parameters {
        string(name: "num_1", defaultValue: "0", description:"Enter First Value")
        string(name: "num_2", defaultValue: "0", description:"Enter Second Value")
        choice(name: "operator", choices: ["add","substract","multiply"], description: "What operation do you want to perform?")
    }

    stages{
        stage("UnitTest"){
            agent{
                docker{
                    image 'qnib/pytest'
                }
            }
            steps{
                python sources/tests.py
                //bat 'py.test --verbose --junit-xml test-reports/results.xml sources/tests.py'
            }
            post{
                always{
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage("Build"){
            agent{
                docker{
                    image 'python:2-alpine'
                }
            }
            steps{
                bat 'python sources/main.py --x %num_1% --y %num_2% --o %operator%'
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
