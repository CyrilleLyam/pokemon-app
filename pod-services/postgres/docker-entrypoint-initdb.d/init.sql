CREATE TABLE pokemon (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    base_experience INT,
    height INT
);

CREATE TABLE abilities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    effect TEXT,
    pokemon_id INT NOT NULL,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id) ON DELETE CASCADE
);

CREATE INDEX idx_pokemon_name ON pokemon(name);
CREATE INDEX idx_abilities_name ON abilities(name);
CREATE INDEX idx_abilities_pokemon_id ON abilities(pokemon_id);
