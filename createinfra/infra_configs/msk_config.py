d = {
    'BrokerNodeGroupInfo': {
        'BrokerAZDistribution': 'DEFAULT',
        'ClientSubnets': [
            'subnet-0d442204ede8447fd','subnet-06588564a4b371207'
        ],
        'InstanceType': 'kafka.t3.small',
        'SecurityGroups': [
            'sg-0c630e0cfb3914178',
        ],
        'StorageInfo': {
            'EbsStorageInfo': {
                'ProvisionedThroughput': {
                    'Enabled': False,
                    # 'VolumeThroughput': 123
                },
                'VolumeSize': 100
            }
        },
        'ConnectivityInfo': {
            'PublicAccess': {
                'Type': 'DISABLED'
            },
            'VpcConnectivity': {
                'ClientAuthentication': {
                    'Sasl': {
                        'Scram': {
                            'Enabled': False
                        },
                        'Iam': {
                            'Enabled': False
                        }
                    },
                    'Tls': {
                        'Enabled':False
                    }
                }
            }
        },
        'ZoneIds': [
            'us-east-1a','us-east-1b'
        ]
    },
    'ClientAuthentication': {
        'Sasl': {
            'Scram': {
                'Enabled': False
            },
            'Iam': {
                'Enabled':  False
            }
        },
        'Tls': {
            'CertificateAuthorityArnList': [],
            'Enabled': False
        },
        'Unauthenticated': {
            'Enabled': True
        }
    },
    'EncryptionInfo': {
        'EncryptionInTransit': {
            'ClientBroker':'TLS_PLAINTEXT',
            'InCluster': True
        }
    },
    'EnhancedMonitoring': 'DEFAULT',
    'KafkaVersion': '3.5.1',
    'LoggingInfo': {
        'BrokerLogs': {
            'CloudWatchLogs': {
                'Enabled': False,
                'LogGroup': ''
            },
            'Firehose': {
                'DeliveryStream': '',
                'Enabled': False
            },
            'S3': {
                'Bucket': '',
                'Enabled': False,
                'Prefix': ''
            }
        }
    },
    'NumberOfBrokerNodes': 2,
    'StorageMode': 'LOCAL'
}


