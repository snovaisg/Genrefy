import os
import librosa

def get_genre(genre):
    folder = "genres_small_fma"
    folder_path = os.path.join(os.getcwd(),folder)
    assert(os.path.isdir(folder_path))
    genre_path = os.path.join(folder_path,genre)
    assert(os.path.isdir(genre_path))
    return genre_path

def get_genre_size(genre):
    genre_path = get_genre(genre)
    return len(os.listdir(genre_path))

def get_music(genre, pos, sr=22050):
    genre_path = get_genre(genre)
    music_path = os.path.join(genre_path, os.listdir(genre_path)[pos])
    assert(os.path.isfile(music_path))
    x, sr = librosa.load(music_path, sr=sr)
    return x,sr