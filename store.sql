CREATE TABLE category(
    id_cat INT NOT NULL AUTO_INCREMENT,
    name_cat VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_cat)
);

CREATE TABLE product(
    id_prod INT NOT NULL AUTO_INCREMENT,
    name_prod VARCHAR(255) NOT NULL,
    description TEXT,
    price INT,
    quantity INT,
    id_cat INT,
    PRIMARY KEY (id_prod),
        CONSTRAINT FK_category_product FOREIGN KEY(id_cat) REFERENCES category(id_cat)
);

INSERT INTO category (name_cat) VALUES("informatique");
INSERT INTO category (name_cat) VALUES("sucreries");
INSERT INTO category (name_cat) VALUES("jeu video");
INSERT INTO category (name_cat) VALUES("biere");


INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("ordinateur SNSV", 999, 8, 1);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("mulot logotich", 10, 18, 1);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("meuporg", 39, 38, 3);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("Assasin Scred", 29, 18, 3);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("chocobon", 2, 49, 2);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("fraises tagada", 2, 45, 2);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("Joufflue", 3, 19, 4);
INSERT INTO product (name_prod, price, quantity, id_cat) VALUES("Matante", 3, 19, 4);