import numpy as np
import librosa
from transformers import pipeline
from joblib import load 
from sklearn import svm

MODEL_CONDITION_AUDIO = "jvalero/wav2vec2-base-vinyl_condition"
MODEL_SCRATCH_DEEP = "DunnBC22/Is_Vinyl_Scratched_Or_Not"

def condition_from_audio(audio_path):
    """Predicts vinyl condition from audio path.

    Args:
        audio_path: Path to the audio file.

    Returns:
        str: Predicted vinyl condition label.
    """
    classifier = pipeline("audio-classification", model=MODEL_CONDITION_AUDIO)
    prediction = classifier(audio_path)
    predicted_condition = prediction[0]["label"]
    return predicted_condition

def scrath_detection(audio_path, kind = "deep"):
    """Predicts scratch in vinyl from audio path.
    
    Args:
        audio_path: Path to the audio file.
        kind: 'deep' or 'SVG', to use Deep Learning model or SVG.
        
    Returns:
        bool: True if a scrathc is present in the audio clip."""
    
    if kind == "deep":
        classifier = pipeline("audio-classification", model = MODEL_SCRATCH_DEEP)
        prediction = classifier(audio_path)
        predicted_condition = prediction[0]["label"]
        result = bool(predicted_condition)

    elif kind == "SVG":
        result = False
        model_linear = load("model_scratch_svg.joblib")
        buffers = librosa.stream(audio_path, block_length = 88200, frame_length = 1, hop_length = 1)
        val = []
        for buffer in buffers:
            for i in buffer:
                val.append([i])
        varray = np.array(val)
        varray.reshape(-1, 1)
        predictions = model_linear.predict(varray)
        result = any(bool(predictions))
    return result
        


