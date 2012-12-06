#!/bin/bash

mvn clean compile install
scp target/bookmanagement.war iggy@192.168.100.10:/home/iggy/
