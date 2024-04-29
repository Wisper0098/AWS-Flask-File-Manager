import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:GMmFWyRV6f91KA9P@file-manager-db-1.cv28gauc472p.eu-north-1.rds.amazonaws.com:5432/file_manager"
    SECRET_KEY="akbDWiH2L5WpsOFe7WQUIxaK"
    USER_PSWD="vxVb5v&("
    ACCESS_KEY_ID="AKIA47CRUIV3EKR7MAE2"
    SECRET_ACCESS_KEY="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"
    AWS_REGION="eu-north-1"
    BUCKET_NAME="file-manager-bucket098"
