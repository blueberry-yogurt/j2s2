from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `users` DROP INDEX `email`;
        ALTER TABLE `users` DROP COLUMN `email`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `users` ADD `email` VARCHAR(255) NOT NULL UNIQUE;"""


MODELS_STATE = (
    "eJztW21P2zAQ/itVP4HEEHS8ad8KlMGAdkC3IRCK3MRtoyZ2iZ2VivW/z3benJdmDZSRUH"
    "9Lz3ex7zmf77HjPtdtbECLbP4g0Kl/qT3XEbAhe4jJN2p1MB5HUi6goGcJRZdpCAnoEeoA"
    "nTJhH1gEMpEBie6YY2pixKTItSwuxDpTNNEgErnIfHShRvEA0qEYyP0DE5vIgE+QBD/HI6"
    "1vQsuIjdM0eN9CrtHpWMjOED0Riry3nqZjy7VRpDye0iFGobaJKJcOIIIOoJC/njouHz4f"
    "ne9m4JE30kjFG6JkY8A+cC0qubsgBjpGHD82GiIcHPBePjW2d/Z3Dj7v7RwwFTGSULI/89"
    "yLfPcMBQLtbn0m2gEFnoaAMcKNh008p9A7GgInGz7ZJgEiG3oSxACyPBQDQQRjNHWWhKMN"
    "njQLogEdcvC2ckD72bw+Om1erzW21rkvmE1mb4q3/ZaGaOK4RjiOASET7BjaEJBhETBThh"
    "VFdHd3EUh3d+djytvioOoO5C5rgKYRPWYt1LRhNqpxywSkhm+6GTyUFGDmg9FB1tRfVXLw"
    "7Z5dtm66zcvv3BObkEdLQNTstnhLQ0inCenaXiIU4Utqv866pzX+s3bXabcEgpjQgSN6jP"
    "S6d3U+JuBSrCE80YAhLYCBNABmxpfu/khahLigB/TRBLDZH2uJZoBhAseEJB3+Q9/w5Pwa"
    "WkBAmw60X7yO2Uum5YzxLJi4gTSKdQRCD+ORDZzRK2E49F9TYST4dJhqPcmRV86KimLCUw"
    "c38LxkSjfZDTspAQgMxKh537ynWLZkcMAwjeaTQCldFQ2sEg2kJrUKccDQQNGViK5gRCHK"
    "4Cpd+DRnCkomVQEyj4a0brsxBhLAtXbZvF2PsZCLTvtroC7Be3TROVQk8OOSQDmw7th4YW"
    "Djliqw7xrYFEnjxwNaoUIsWfy7GpckfEsoyKkdURzDNIAn2IHmAJ3DqcDxjI0IID2rDCeO"
    "7cqH3zxqy8QOmITMTp4azD3mFKQeM2neHDWPW/XZIrvIJW2g1I4he8cQQpKxaZDhmr9viA"
    "VI7RzKtlBt5OwcFD37EFU8Tc8eXUxhsToum6xSIVfsR7Gf92E/qYRdAmxXwXuqi5u8EBWl"
    "jW9+tppHl1IUM/+sNX4WvlzidB+moeip/qCYlGJSikm9gEl5mVooLWSTVSIFikkpJvX+TM"
    "oIvnS+ErYKXjxI4iYvRGViUlcuJL7PKRIVtuXyp0dZSx05lWxNyyNKQeQ0Cp8KfW1NGapv"
    "rtE31wL3s94ysZvQMfVhVlr7LblJDSIdldIVSunf0CH+WrzoDRTJpCpp/B/uoPDUKACir1"
    "5NALe3FrnGzbTmAijaFrzE8+2m0y56iccwdVr7U7NMUtLtRw5+3N/8wpKsIRvxnTN/QYkK"
    "i3esmUkX/fPOPK4YqKiqUqGqsnK3GhdaEBs5C2KjwIKobjW+HcNO312BhtbLOJNYgT8ALL"
    "8ozP4CDRZW/w=="
)
