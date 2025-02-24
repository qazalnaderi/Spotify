CREATE DATABASE spotify;
\c spotify;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    is_verified BOOLEAN NOT NULL DEFAULT false,
    is_artist BOOLEAN NOT NULL DEFAULT false,
    username VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL, 
    profile_url TEXT,
    library_id SERIAL UNIQUE,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE follows (
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    following_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    followed_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY (user_id, following_id)
);


CREATE TABLE songs (
    song_id SERIAL PRIMARY KEY,
    song_name VARCHAR(100) NOT NULL,
    artist_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    picture_url TEXT,
    file_url TEXT NOT NULL, 
    duration INT NOT NULL, 
    release_date DATE,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(100) NOT NULL,
    album_desc VARCHAR(255),
    picture_url TEXT,
    artist_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    release_date DATE,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE album_song (
    album_id INT REFERENCES albums(album_id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(song_id) ON DELETE CASCADE,
    PRIMARY KEY (album_id, song_id)
);

CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    playlist_name VARCHAR(100) NOT NULL,
    playlist_desc VARCHAR(255),
    picture_url TEXT,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE playlist_song (
    playlist_id INT REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(song_id) ON DELETE CASCADE,
    PRIMARY KEY (playlist_id, song_id)
);

CREATE TABLE libraries (
    library_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE REFERENCES users(user_id) ON DELETE CASCADE
);


CREATE TABLE library_songs (
    library_id INT REFERENCES libraries(library_id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(song_id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY (library_id, song_id)
);

CREATE TABLE library_albums (
    library_id INT REFERENCES libraries(library_id) ON DELETE CASCADE,
    album_id INT REFERENCES albums(album_id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY (user_id, album_id)
);

CREATE TABLE library_playlists (
    library_id INT REFERENCES libraries(library_id) ON DELETE CASCADE,
    playlist_id INT REFERENCES playlists(playlist_id) ON DELETE CASCADE,
    added_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY (user_id, playlist_id)
);
