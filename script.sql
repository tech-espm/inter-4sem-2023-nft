
-- -----------------------------------------------------
-- Schema webScraping
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS webScraping DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE webScraping ;

-- -----------------------------------------------------
-- Table collection
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS collection (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    image VARCHAR(200) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
    UNIQUE INDEX nome_UNIQUE (name ASC) VISIBLE);


-- -----------------------------------------------------
-- Table dailyReport
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS dailyReport (
    id INT NOT NULL AUTO_INCREMENT,
    ranking INT NOT NULL,
    collection_name VARCHAR(100) NOT NULL,
    volume FLOAT NOT NULL,
    volumeChange FLOAT NOT NULL,
    tokenCount INT NOT NULL,
    onSaleCount INT NOT NULL,
    floorSale FLOAT NOT NULL,
    ownerCount INT NOT NULL,
    date DATE NOT NULL,
    collection_id INT NOT NULL,


    PRIMARY KEY (id),
    UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
    INDEX collection_id_date_idx (collection_id ASC, date ASC) VISIBLE,
	INDEX date_ranking_idx (date ASC, ranking ASC) VISIBLE,
    CONSTRAINT collection_id
    FOREIGN KEY (collection_id)
    REFERENCES collection (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
