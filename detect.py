from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN

filename = '/samuel/min_samuel_0.png'
pixels = pyplot.imread(filename)

detector = MTCNN()

faces = detector.detect_faces(pixels)

for face in faces:
    print(face)