import numpy as np
import lightgbm as lgb

import thrember

model = lgb.Booster(model_file="/home/muaviz/dev/project/AnubisAV/models/EMBER2024_all.model")

extractor = thrember.features.PEFeatureExtractor()

with open("/home/muaviz/Downloads/windows.exe", "rb") as f:
    byt = f.read()

features = extractor.feature_vector(byt)

features = features.reshape(1, -1)
prob = model.predict(features)


print(f"{prob[0]:.4f}")
