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
    "eJztWl1P2zAU/StVn0DaEGQU0N7SUkYHtBtkG2KaIjdx06iJHRJnpWL977Od7881rBsJ5C"
    "29vje+9/jG58TpY9fEKjScvS8OtLvvO49dBExILxL2N50usKzIygwETA3u6FIPbgFTh9hA"
    "IdQ4A4YDqUmFjmLrFtExolbkGgYzYoU66kiLTC7S710oE6xBMueJfP9BzTpS4QN0gp/WQp"
    "7p0FATeeoqm5vbZbKyuG2EyBl3ZLNNZQUbrokiZ2tF5hiF3joizKpBBG1AILs9sV2WPsvO"
    "LzOoyMs0cvFSjMWocAZcg8TK3RADBSOGH83G4QVqbJa3wsHh8eHJu6PDE+rCMwktx2uvvK"
    "h2L5AjMJa6az4OCPA8OIwRbmzZ+HUGvcEc2PnwxWNSINLU0yAGkJWhGBgiGKPW2RKOJniQ"
    "DYg0Mmfg7ZeA9lW8HpyL1zvC/i6rBdNm9lp87I8IfIjhGuFoAcdZYluV58CZVwEzE9hQRH"
    "u9TSDt9YoxZWNJUBUbspJlQLKIntIRopswH9VkZApS1Q/dCy5qCjCtQZ0gY+XvKiX4SqOr"
    "4Y0kXn1ilZiOc29wiERpyEYEbl2lrDtHqaUIb9L5NpLOO+xn524yHnIEsUM0m88Y+Ul3XZ"
    "YTcAmWEV7KQI1tgIE1AGbNtu7ZIrYJMcMUKIsloN2fGIk6QNWBrUMnu/x9P/Ds4hoagEOb"
    "XWifvE7pTVb1XON10LiBNVrrCIQpxgsT2Iu/hKHv36ZhSLA2wQIuapzskCmYaQtAQONZs7"
    "nZTInOyNE7YcsUC55Ya7aSp0mSh+jEqKR3woCWmiNqxohAlMPLEnwoaMFYSFOALKPc4a2U"
    "YNsArp0r8XY3wbiXk/GHwD0G7+By0m8Fz8sVPPGFdS31iQubjGwX9lkXNiPN2KuwXImIYx"
    "F/ZuOaLN8WCDmj/pMYZgE8wzbUNXQBVxzHEc0IICWPhlNHVPXDr0jaUrMNlqGyi7cGLY8W"
    "BYmnTMSbgXg67K6L35j+pUgO3xtydHL8naJYKideYFqxXLdns0wst4rkRRBXVpHcu5jAat"
    "QVD3lN3NUSfkv4z0P4mQd2C7B9Du7TXNziG1GdlJIIbV2Z5+kkf6RUJYHIp5VINdvNyiTS"
    "T2g7/sH7pieKsZCmHIX9hzNF9mhUANF3byaAB/ubfIKmXoUA8rEND2U/3kzGVQ9lVV0hnV"
    "8dQ3dqqlJK8GP1lh/Ops9hUwKb3aCfp2Keh1g8zs7hlZDMi2kl1A0tqzSJVV7dV6qNNkSh"
    "ZEMUKmyI7Veqil+pnvTvjeDcD6rydNX+eWErpLD+DTdHYuY="
)
