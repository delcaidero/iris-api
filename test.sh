curl -d '{"SepalLengthCm":6.2,"SepalWidthCm":3.4,"PetalLengthCm":5.4,"PetalWidthCm":2.3}' \
-H "Content-Type: application/json" \
-X POST http://0.0.0.0:8000/predict

#curl -d '{"SepalLengthCm": 4.9, "SepalWidthCm": 3., "PetalLengthCm":1.4, "PetalWidthCm":0.2}' \
#-H "Content-Type: application/json" \
#-X POST http://0.0.0.0:8000/predict
