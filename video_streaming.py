from flask import Flask, render_template, Response
from camera import Camera
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        img = cv2.flip(frame, 1)
        cv2.imwrite('cap.jpg',img)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('cap.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)