import boto3

client = boto3.client('s3')

clientResponse = client.list_buckets()
client.upload_file(Filename="C:/Users/Lutfi/Downloads/face detection/capture/Capturing.jpg", Bucket='esp32-rekognition-145954723858', Key="C:/Users/Lutfi/Downloads/face detection/capture/Capturing.jpg")

# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')