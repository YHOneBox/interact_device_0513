from flask import Flask, render_template, jsonify, request, redirect, url_for
#import numpy as np
#import random
import base64

app = Flask(__name__)

# 全局變量，用於存儲捕捉到的臉部圖像和臉部座標
face_image_path = None
face_coordinates = None

@app.route('/')
def prelude():
    return render_template('prelude.html')

@app.route('/role')
def role():
    return render_template('role.html')

@app.route('/final')
def final():
    return render_template('final.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/run_python_program')
def run_python_program():
    return redirect(url_for('index'))

@app.route('/capture', methods=['GET', 'POST'])
def capture():
    # Removed or commented out old server-side capture code
    return 'Capture route disabled'

@app.route('/save_face', methods=['POST'])
def save_face():
    # 接收前端傳來的base64影像並儲存
    data = request.get_json()
    face_data = data.get('faceData')
    if face_data:
        img_data = base64.b64decode(face_data.split(',')[1])
        with open('static/face.jpg', 'wb') as f:
            f.write(img_data)
        return jsonify({'faceImagePath': 'static/face.jpg'}), 200
    return 'No face data received', 400

@app.route('/canvas_data', methods=['POST'])
def canvas_data():
    global face_image_path, face_coordinates

    # 檢查是否捕捉到了臉部圖像和臉部座標
    if face_image_path is None or face_coordinates is None:
        return 'No face captured'

    # 在這裡處理Canvas的數據，例如保存繪製的圖像等

    return 'Canvas data received'

@app.route('/save_canvas', methods=['POST'])
def save_canvas():
    # 接收前端發送的畫布數據
    data = request.get_json()
    canvas_data = data.get('canvasData')

    # 將 base64 字符串轉換為圖片並保存到 static 資料夾中
    if canvas_data:
        img_data = base64.b64decode(canvas_data.split(',')[1])
        with open('static/canvas.jpg', 'wb') as f:
            f.write(img_data)

        return 'Canvas data saved', 200
    else:
        return 'No canvas data received', 400
    

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    canvas_data = data.get('canvasData')

    if canvas_data:
        try:
            img_data = base64.b64decode(canvas_data.split(',')[1])
            sequential_id = request.headers.get('Sequential-ID', '0')
            try:
                sequential_id = int(sequential_id)
            except ValueError:
                sequential_id = 0
            formatted_id = f'{sequential_id:03}'
            with open(f'static/character/{formatted_id}.png', 'wb') as f:
                f.write(img_data)
            return 'Canvas data saved', 200
        except Exception as e:
            return f'Error: {str(e)}', 400
    else:
        return 'No canvas data received', 400

@app.route('/retry', methods=['GET'])
def retry():
    global face_image_path, face_coordinates
    face_image_path = None
    face_coordinates = None
    return redirect(url_for('capture'))

@app.route('/drawing')
def drawing():
    return render_template('drawing.html')
    
if __name__ == '__main__':
    app.run(debug=True)
