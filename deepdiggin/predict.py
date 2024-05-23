from transformers import pipeline

MODEL_NAME = "jvalero/wav2vec2-base-vinyl_condition"

def condition_from_audio(audio_path):
    """Predicts vinyl condition from audio path.

    Args:
        audio_path: Path to the audio file.

    Returns:
        str: Predicted vinyl condition label.
    """
    classifier = pipeline("audio-classification", model=MODEL_NAME)
    prediction = classifier(audio_path)
    predicted_condition = prediction[0]["label"]
    return predicted_condition
