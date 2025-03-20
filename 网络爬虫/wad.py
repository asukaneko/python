import wad.detection

det = wad.detection.Detector()
url = "https://{}".format(input("url:"))
print(det.detect(url))
