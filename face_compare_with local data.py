import boto3


sourceFile = 'images/obama.jpg'           #sourceFile,targetFile will contain the path of the image stored locally
targetFile = 'images/obama2.jpg'
client = boto3.client('rekognition')

imageSource = open(sourceFile, 'rb')
imageTarget = open(targetFile, 'rb')

response = client.compare_faces(SimilarityThreshold=0,
                                SourceImage={'Bytes': imageSource.read()},
                                TargetImage={'Bytes': imageTarget.read()})
for record in response['FaceMatches']:
    face = record
    confidence = face['Face']

    print("Matched With {}""%"" Similarity".format(face['Similarity']))
    print("With {}""%"" Confidence".format(confidence['Confidence']))

    c = float(format(face['Similarity']))

    if (c > 95):
        {
            print("Matched")
        }
    else:
        print("Not a match")

imageSource.close()
imageTarget.close()
