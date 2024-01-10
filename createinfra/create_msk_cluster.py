import boto3

from infra_configs import msk_config


conf = msk_config.d

def create_msk_cluster():
   
    # AWS credentials and region
    region = 'us-east1'

    # MSK configuration
    
    # Create MSK client
    msk_client = boto3.client('kafka',region_name="us-east-1")
#,region_name="us-east1"
    # Create MSK cluster
    response = msk_client.create_cluster_v2(
    ClusterName = "kakfka-test",Provisioned = conf
    )

    print("Cluster ARN:", response['ClusterArn'])
    print("Cluster Name:", response['ClusterName'])
    print("Current State:", response['State'])
    
if __name__ == "__main__":
    create_msk_cluster()
