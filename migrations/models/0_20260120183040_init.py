from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlW1v0zAQx79KlFedBNNWugfxLitFK6It2gJMQyhyEze16thZfGGrRr87Piep0/RBGx"
    "qMSbxL/vd3fPdzfHfvJjKiXO1/VjRz3zr3riAJ1Q8r+ivHJWlqVRSAjLkx5tphFDJWkJEQ"
    "tDghXFEtRVSFGUuBSaFVkXOOogy1kYnYSrlgNzkNQMYUpiaRb9+1zERE76iqXtNZMGGURy"
    "t5sgj3NnoA89RofQHvjRF3Gweh5HkirDmdw1SKpZsJQDWmgmYEKH4eshzTx+zKMquKikyt"
    "pUixtiaiE5JzqJX7QAahFMhPZ6NMgTHu8rp92DnpnL457pxqi8lkqZwsivJs7cVCQ2Douw"
    "sTJ0AKh8FoudGEML6Orjsl2WZ2ywUNfDrpJr4K1rPyS8hdwKmIYYrQjo520PriXXTPvYuW"
    "du1hLVL/xsXPPSxD7SKGSC3CMKNYcEBgneM7HQGW0M0sV1c2gEbl0v3q4XfwVoLla+/kEw"
    "HWNUQjwefl2e3g6/cHvUvfG3zCShKlbrhB5Pk9jLSNOm+orePGUSw/4nzt++cOvjrXo2HP"
    "EJQK4szsaH3+tYs5kRxkIORtQKLab1apFZgFNpjJrHZVUBiTcHZLsihYi8i23OZdDyXtpK"
    "kQQWJzLAgX0yz7rUczFk43deIysrMXE+v534xfUDP+oUcopvSIdlxb8jQN+S90jD/fkvFq"
    "PAJiaX+ZAA8PDh4AULu2AjSxxkyTAqjYMNA+XI6GW4aZXdKcZCwE56fDmVq71P8G0B38sN"
    "6VcVVhaw28qybR7sfRWXMO4QfONN1nHSyLX7CIx9M="
)
