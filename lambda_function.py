import json
import boto3

ec2 = boto3.resource('ec2')
s3 = boto3.resource('s3')

def lambda_handler(event, context):

 """ Possible EC2 instance states: pending, running, shutting-down, terminated, stopping, stopped. """
 filters = [
   {
    'Name': 'instance-state-name',
    'Values': ['running']
   }
  ]
 
 instances = ec2.instances.filter(Filters = filters)
 
 RunningInstances = []
 
 for instance in instances:
  RunningInstances.append(instance.id)
 
 instanceList = json.dumps(RunningInstances)
 
 s3.Object('aws-list-ec2-instances','instanceList.txt').put(Body = instanceList)
 
 return {
  "statusCode": 200,
  "body": instanceList
 }



**********************************

