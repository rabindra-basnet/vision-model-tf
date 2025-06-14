# /// script
# dependencies = [
#   "roboflow",
# ]
# ///

from roboflow import Roboflow
rf = Roboflow(api_key="Xb0vLx7TcbYWQNB4s04j")
project = rf.workspace("ashaya").project("images_jaxa")
version = project.version(1)
dataset = version.download("voc")
                


