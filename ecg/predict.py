from builtins import str
import numpy as np
from joblib import Memory
memory = Memory(cachedir='./cache')


@memory.cache
def get_ensemble_pred_probs(model_paths, x):
    print("Averaging " + str(len(model_paths)) + " model predictions...")

    def get_model_pred_probs(model_path, x):
        from keras.models import load_model
        model = load_model(model_path)
        probs = model.predict(x, verbose=1)
        return probs

    all_model_probs = [get_model_pred_probs(model_path, x)
                       for model_path in model_paths]
    probs = np.mean(all_model_probs, axis=0)
    return probs
