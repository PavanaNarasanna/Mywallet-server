from .config import AwsS3Config
from boto3.session import Session


def get_session():
    return Session(aws_access_key_id=AwsS3Config.ACCESS_KEY,
                   aws_secret_access_key=AwsS3Config.SECRET_KEY)


def get_all_files_from_s3():
    client = get_session().client('s3')
    all_s3_files = client.list_objects(Bucket=AwsS3Config.BUCKET_NAME)
    return_files = []
    for s3_file in all_s3_files['Contents']:
        return_files.append(s3_file['Key'])

    return return_files


def get_file_from_s3(filename):
    client = get_session().client('s3')
    pdf = client.get_object(Bucket=AwsS3Config.BUCKET_NAME, Key=filename)
    return pdf


def send_file_to_s3(file, filename):
    client = get_session().client('s3')
    response = client.put_object(Bucket=AwsS3Config.BUCKET_NAME, Key=filename, Body=file)
    return response
