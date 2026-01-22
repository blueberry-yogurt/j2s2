from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `diary_bookmark` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `diary_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    UNIQUE KEY `uid_diary_bookm_user_id_5e6366` (`user_id`, `diary_id`),
    CONSTRAINT `fk_diary_bo_diaries_451af50b` FOREIGN KEY (`diary_id`) REFERENCES `diaries` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_diary_bo_users_3e102d0d` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `diary_bookmark`;"""


MODELS_STATE = (
    "eJztW21P2zAQ/itVP4HEJuiAoX0rUDY2aAd0GwKhyE1MazWxS+wMKtb/Ptt5c16aNdCOBP"
    "wtPd/Fvud8vseO+9h0iAVt+v4HhW7zU+OxiYED+UNCvtFogskklgoBAwNbKnpcQ0rAgDIX"
    "mIwLb4FNIRdZkJoumjBEMJdiz7aFkJhcEeFhLPIwuvOgwcgQspEcyPUNFyNswQdIw5+TsX"
    "GLoG0lxoks0beUG2w6kbJjzI6kouhtYJjE9hwcK0+mbERwpI0wE9IhxNAFDIrXM9cTwxej"
    "C9wMPfJHGqv4Q1RsLHgLPJsp7i6IgUmwwI+PhkoHh6KXd62t7Y/bex92t/e4ihxJJPk489"
    "2LffcNJQLdfnMm2wEDvoaEMcZNhE0+Z9A7GAE3Hz7VJgUiH3oaxBCyIhRDQQxjPHWWhKMD"
    "Hgwb4iEbCfA2C0D72T4/+NI+X2ttrgtfCJ/M/hTvBi0t2SRwjXGEDkB2GRAjg+UguPJ5mM"
    "RvZ2cRAHd25iMo2pIQTgCl98S1jBGgozJQZgxrOilXAarpQuGyAVgW0UPewpAD81FNWqYg"
    "tQLT9+FDRQHmPlg9bE+DhCjAt3982rnot0+/C08cSu9sCVG73xEtLSmdpqRru6lQRC9p/D"
    "ruf2mIn42rXrcjESSUDV3ZY6zXv2qKMQGPEQOTewNYSu6G0hCYmah+t2NlHReCATDH94DP"
    "/kRLPAMsBFwEaTb8+4Hh0bdzaAMJbTbQQf0/5C+ZVjPGs3DihtI41jEIA0LGDnDHz4RhP3"
    "hNjZEQ02FqDBRHnjkraoqJSB3SIvOSKdvktJy0BGAwlKMWfYueEtmSQ6OjNJrPo5V01Uy6"
    "TkyaIWaXotGRgaYrMV0hmEGcw1X68GHOFFRM6gJkEQ3pXPYTDCSEa+20fbmeYCEnve7nUF"
    "2B9+Ckt69J4OslgWpgvYn1xMAmLXVgXzSwGZImTliMUoVYsfh3Na5I+JZQkDM7oiSGWQCP"
    "iAvREH+DU4njMR8RwGZeGU6dfFYPv3nUlotdcB8xO3VqcPe4U5D5zKR9cdA+7DRni+wil7"
    "SB0juG/B1DBEnOpkGFa/6+IREgvXOo2kK1UbBz0PTsVVTxLD278wiD5eq4avKWCrlmP5r9"
    "vAz7ySTsEmA7C99TX9zUhagsbVz52WoRXcpQzOKz1uRZ+HKJ03WUhrKn5o1mUppJaSb1BC"
    "blZ2qptFBN3hIp0ExKM6mXZ1JW+KXzmbDV8OJBGjd1IaoSkzrzIA18zpCoqK2QP92pWvrI"
    "qWJrWhFRCiNnMPhQ6mtrxlB/c42/uZa4n7XKxG5DF5mjvLQOWgqTGsQ6OqVrlNK/oUuDtX"
    "jRGyiKSV3S+D/cQRGpUQLEQL2eAG5tLnITnmvNBVC2LXiJ5+tFr1v2Eo+FTNb407ARrej2"
    "owA/4W9xYUnXkI3kzlm8oEKFxT/WzKWLwXlnEVcMVXRVqVFVeXO3GhdaEFsFC2KrxIKobz"
    "WujmFn765AyxjknEm8gT8ALL8ozP4CVc29Nw=="
)
