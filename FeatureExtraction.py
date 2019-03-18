def extract_features(x,sr):

    def extract_zero_crossing_rate(x, sr):
        """
        inputs
        --------------------------
        x    : np.ndarray [shape=(n,)]
        audio time series

        sr   : number > 0 [scalar]
        sampling rate of `x`

        outputs
        --------------------------
        y    : int
        zero crossing rate normalized by length of the clip
        """

        zero_crossings = librosa.zero_crossings(x, pad=False)
        #normalize by time span
        duration = librosa.core.get_duration(x,sr)
        zero_crossings = sum(zero_crossings) / duration
        return zero_crossings
    
    
    