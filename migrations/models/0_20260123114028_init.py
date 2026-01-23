from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(20) NOT NULL,
    `password_hash` VARCHAR(255) NOT NULL,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `diaries` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `content` LONGTEXT NOT NULL,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_diaries_users_fdac245e` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `diary_bookmark` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `diary_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    UNIQUE KEY `uid_diary_bookm_user_id_5e6366` (`user_id`, `diary_id`),
    CONSTRAINT `fk_diary_bo_diaries_451af50b` FOREIGN KEY (`diary_id`) REFERENCES `diaries` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_diary_bo_users_3e102d0d` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `question` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `question_text` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `quotes` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `content` LONGTEXT NOT NULL,
    `author` VARCHAR(255)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `bookmarks` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `quote_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_bookmark_quotes_65941675` FOREIGN KEY (`quote_id`) REFERENCES `quotes` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_bookmark_users_f866d0ef` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztW21P2zAQ/itVP4HEEHS8ad8KlMGAdkC3IRCK3MRtoyZ2iZ2VivW/z3benJdmTSkjAX"
    "9Lz3ex7zmf77HjPtdtbECLbP4g0Kl/qT3XEbAhe4jJN2p1MB5HUi6goGcJRZdpCAnoEeoA"
    "nTJhH1gEMpEBie6YY2pixKTItSwuxDpTNNEgErnIfHShRvEA0qEYyP0DE5vIgE+QBD/HI6"
    "1vQsuIjdM0eN9CrtHpWMjOED0Riry3nqZjy7VRpDye0iFGobaJKJcOIIIOoJC/njouHz4f"
    "ne9m4JE30kjFG6JkY8A+cC0qubsgBjpGHD82GiIcHPBePjW2d/Z3Dj7v7RwwFTGSULI/89"
    "yLfPcMBQLtbn0m2gEFnoaAMcKNh008p9A7GgInGz7ZJgEiG3oSxACyPBQDQQRjNHVWhKMN"
    "njQLogEdcvC2ckD72bw+Om1erzW21rkvmE1mb4q3/ZaGaOK4RjiOASET7BjaEJBhETBThh"
    "VFdHd3EUh3d+djytvioOoO5C5rgKYRPWYt1LRhNqpxywSkhm+6GTyUFGDmg9FB1tRfVXLw"
    "7Z5dtm66zcvv3BObkEdLQNTstnhLQ0inCenaXiIU4Utqv866pzX+s3bXabcEgpjQgSN6jP"
    "S6d3U+JuBSrCE80YAhLYCBNABmxpfu/khahLigB/TRBLDZH2uJZoBhAseEJB3+Q9/w5Pwa"
    "WkBAmw60X7yO2Uum5YzxLJi4gTSKdQRCD+ORDZzRC2E49F9TYST4dJhqPcmRF86KimLCUw"
    "c38LxkSjfZDTspAQgMxKh537ynWLZkcMAwjeaTQCldFQ2sEg2kJrUKccDQQNGViK5gRCHK"
    "4Cpd+DRnCkomVQEyj4a0brsxBhLAtXbZvF2PsZCLTvtroC7Be3TROVQk8P2SQDmw7thYMr"
    "BxSxXYNw1siqTx4wGtUCGWLP5djUsSvhUU5NSOKI5hGsAT7EBzgM7hVOB4xkYEkJ5VhhPH"
    "duXDbx61ZWIHTEJmJ08N5h5zClKPmTRvjprHrfpskV3kijZQaseQvWMIIcnYNMhwzd83xA"
    "Kkdg5lW6g2cnYOip69iyqepmePLqawWB2XTT5SIVfsR7Gft2E/qYRdAWxXwXuqi5u8EBWl"
    "ja9+tppHl1IUM/+sNX4WvlridB+moeip/qCYlGJSikktwaS8TC2UFrLJRyIFikkpJvX2TM"
    "oIvnS+ELYKXjxI4iYvRGViUlcuJL7PKRIVtuXyp0dZSx05lWxNyyNKQeQ0Cp8KfW1NGapv"
    "rtE31wL3s14zsZvQMfVhVlr7LblJDSIdldIVSunf0CH+WrzoDRTJpCpp/B/uoPDUKACir1"
    "5NALe3FrnGzbTmAijaFrzE8+2m0y56iccwdVr7U7NMUtLtRw5+3N/8wpKsIRvxnTN/QYkK"
    "i3esmUkX/fPOPK7IVNTHycqVFXUj7zVu5AGX4ZJxrJBTZkKLpTD1Z131K/VS/4EIjvihof"
    "UyTiU+wF8AVl8WZn8BrlJYJw=="
)
