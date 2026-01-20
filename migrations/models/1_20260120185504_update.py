from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `users` ADD `password_hash` VARCHAR(255) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `users` DROP COLUMN `password_hash`;"""


MODELS_STATE = (
    "eJztlm1vmzAQx78K4lUnbVWbpQ/aO5plaqYlmVr2oE4TuoADVoxNsVkadfnu8xmIE/KgRp"
    "rURuo7+N//8N0P7OPRTUVEmDz+JknufnAeXQ4p0Rcr+lvHhSyzKgoKRswYC+0wCoykyiFU"
    "WhwDk0RLEZFhTjNFBdcqLxhDUYTaSHlspYLT+4IESsREJaaQX7+1THlEHoisb7NJMKaERS"
    "t10gjXNnqgZpnRelx9MkZcbRSEghUpt+ZsphLBF27KFaox4SQHRfDxKi+wfKyuarPuqKzU"
    "WsoSl3IiMoaCqaV2n8ggFBz56WqkaTDGVd61TtsX7cv35+1LbTGVLJSLedme7b1MNAQGvj"
    "s3cVBQOgxGy42kQNk6uk4C+WZ2i4QGPl10E18N61n5pfAQMMJjlSC0s7MdtL57N51r7+ZI"
    "u95gL0J/xuXHPahCrTKGSC3CDKScijwKEpDJPijXEv8P0lqwTO0+PBioYU6w5QDUOtGPOq"
    "JoSjZTXc1sII2q1OP64oUC1j1EQ85m1YbYwdfv9bu3vtf/ip2kUt4zg8jzuxhpGXXWUI/O"
    "G69i8RDnR8+/dvDWuRsOuoagkCrOzYrW59+5WBMUSgRcTAOIlvZurdZg5nhqjydL5w8KIw"
    "gnU9Bf/1pEtMQ273oobaVNBTjE5rUgXCyzGmIeyWmYbBpvVWTngAPreZ1wBzTh/uj/Eixp"
    "j4N5KeX1SF6AxK2xB8TKfpgAT09OngBQu7YCNLHGTBNcEb5hoH2+HQ62DDOb0pxkNFTOX4"
    "dRubapXwbQHfyw35VxVWM76ns/m0Q7X4ZXzTmED7jSdJ91sMz/ASa9NYw="
)
