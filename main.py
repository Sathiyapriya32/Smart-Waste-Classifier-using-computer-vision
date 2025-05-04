import os
import cv2
import cvzone
from cvzone.ClassificationModule import Classifier

# Load model and labels
classifier = Classifier('Resources/Model/keras_model.h5', 'Resources/Model/labels.txt')

# Start webcam
cap = cv2.VideoCapture(0)

# Load arrow image
imgArrow = cv2.imread('Resources/arrow.png', cv2.IMREAD_UNCHANGED)

# Load waste images (1 to 8)
imgWasteList = []
pathFolderWaste = "Resources/Waste"
wasteList = sorted(os.listdir(pathFolderWaste))  # Ensure order is correct
for path in wasteList:
    if path.endswith(".png"):
        imgWasteList.append(cv2.imread(os.path.join(pathFolderWaste, path), cv2.IMREAD_UNCHANGED))

# Load bin images (1.png = Recyclable, 2.png = Hazardous, etc.)
imgBinsList = []
pathFolderBins = "Resources/Bins"
binList = sorted([f for f in os.listdir(pathFolderBins) if f.endswith('.png')],
                 key=lambda x: int(x.split('.')[0]))  # Sort numerically by filename

for path in binList:
    imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

# Mapping of classID to bin index (0-based index)
# 0 = Nothing (skip), 1 = Cans, 2 = Newspaper, ..., 8 = Apple
# Bin mapping:
# 1: Recyclable → index 0
# 2: Hazardous  → index 1
# 3: Food       → index 2
# 4: Residual   → index 3
classDic = {
    0: None,   # Nothing
    1: 0,      # Cans → Recyclable
    2: 0,      # Newspaper → Recyclable
    3: 3,      # Old shoes → Residual
    4: 3,      # Plastic pen → Residual
    5: 1,      # Disinfectant → Hazardous
    6: 1,      # Battery → Hazardous
    7: 2,      # Vegetable → Food
    8: 2       # Apple → Food
}

while True:
    success, img = cap.read()
    imgResize = cv2.resize(img, (454, 340))

    # Background image
    imgBackground = cv2.imread('Resources/background.png')

    # Get prediction from the model
    prediction = classifier.getPrediction(img)
    classID = prediction[1]

    print(f"Detected Class ID: {classID}")

    if classID != 0:
        # Overlay waste image
        if 1 <= classID <= len(imgWasteList):
            imgBackground = cvzone.overlayPNG(imgBackground, imgWasteList[classID - 1], (909, 127))
        imgBackground = cvzone.overlayPNG(imgBackground, imgArrow, (978, 320))

        # Get corresponding bin index
        classIDBin = classDic.get(classID, 0)  # default to 0 (Recyclable) if not found

        # Overlay correct bin image
        if classIDBin is not None and classIDBin < len(imgBinsList):
            imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin], (895, 374))

    # Show camera feed on background
    imgBackground[148:148 + 340, 159:159 + 454] = imgResize

    # Show final output
    cv2.imshow("Output", imgBackground)
    cv2.waitKey(1)
