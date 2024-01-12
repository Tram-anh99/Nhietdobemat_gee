import ee
from flask import Flask, jsonify

app = Flask(__name__)

# Khởi tạo Earth Engine
ee.Initialize()

@app.route('/')
def hello_world():
    # Sử dụng Earth Engine ở đây
    image = ee.Image("LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318")
    band_info = image.getInfo()
    return jsonify(band_info)

if __name__ == '__main__':
    app.run(debug=True)
