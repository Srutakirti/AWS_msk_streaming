sudo yum update
sudo yum install java-11-amazon-corretto-devel
#/usr/lib/jvm/java-11-openjdk
wget https://archive.apache.org/dist/kafka/3.5.1/kafka_2.13-3.5.1.tgz
tar -xzf kafka_2.13-3.5.1.tgz
java -jar my.jar --config  eventsim/examples/alt-example-config.json --from 365 --nusers 1000 --growth-rate 0.01 data/fake.json
sudo yum install java-1.8.0