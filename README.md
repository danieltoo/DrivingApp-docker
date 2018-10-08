# Welcome to DrivingApp-docker!

**Clone this repo**

    git clone https://github.com/smartsdkCenidet/DrivingApp-docker.git

**Run docker-compose**

    cd ./DrivingApp-docker
    docker-compose up -d

**Docker Containers**

| Images | Version | Container<br>name | Ports | Depends on |
|--|--|--| --|--|
| **fiware/orion**| **1.15.1** | orion | **1026** | mongo |
| **mongo** | **3.2** | mongo | **27017** |  |
| **smartsdk/quantumleap** | **latest** | quantumleap | **8668** | orion, mongo, crate |
| **crate** | **3.0.5** | crate | **4200<br>4300** |  |
| **grafana/grafana** | **latest** | grafana | **3000** | crate |
| **redis** | **latest** | redis | **6379** |  |
| **mariadb** | **latest** | mariadb | **3306** |  |
| **cenidetiot/smartsecurity-web-service** | **latest** | smartservice | **4005** | mariadb, crate, orion, idm |
| **cenidetiot/smartsecurity-notifications** | **latest** | notifications | **3001** | smartservice |
| **ging/fiware-idm** | **latest** | idm | **5000<br>8000** |  |