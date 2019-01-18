import boto3


def face_comparision():
    client = boto3.client('rekognition','ap-south-1')
    response = client.compare_faces(
        SourceImage={
            'S3Object': {
                'Bucket': 'datacompare',
                'Name': 'selena.jpg'
            }
        },
        TargetImage={
            'S3Object': {
                'Bucket': 'datacompare',
                'Name': 'obama1.jpg'
            }
        },SimilarityThreshold=0

    )
    return (response['FaceMatches'])


face_comparision()
for record in face_comparision():
    face = record
    confidence = face['Face']

    print("Matched With {}""%"" Similarity".format(face['Similarity']))
    print("With {}""%"" Confidence".format(confidence['Confidence']))

    c = float(format(face['Similarity']))


    if(c > 95):{
            print("Matched")
        }
    else:
        print("Not a match")



