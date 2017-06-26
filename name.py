import os

root = os.getenv('MODEL_PATH', "")
network_name = "red-fire-cifar"
model_path = os.path.join(root, "models", network_name)
