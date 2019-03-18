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
    x, sr = librosa.load(music_path, sr=sr,duration=30)
    return x,sr

def get_music_path(genre, pos):
    genre_path = get_genre(genre)
    music_path = os.path.join(genre_path, os.listdir(genre_path)[pos])
    assert(os.path.isfile(music_path))
    return os.path.basename(music_path)
    
def extract_features():
    header = 'filename chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
    for i in range(1, 21):
        header += f' mfcc{i}'
    header += ' label'
    header = header.split()

    file = open('data.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header);
    genres = "pop classical country disco hiphop jazz metal pop reggae rock blues".split()
    for g in genres:
        print(g)
        for pos in range(get_genre_size(g)):
            y, sr = get_music(g,pos)
            songname = utils.get_music_path(g,pos)
            chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
            spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
            spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
            zcr = librosa.feature.zero_crossing_rate(y)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            to_append = f'{songname} {np.mean(chroma_stft)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
            for e in mfcc:
                to_append += f' {np.mean(e)}'
            to_append += f' {g}'
            file = open('data.csv', 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append.split());
            if pos % 5 == 0:
                print(pos)
