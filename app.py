@app.route('/', methods=['GET', 'POST'])
def index():
    """Video streaming home page."""
    if request.method == 'POST':
        if request.form.get('action1') == 'Bottone1':
            Acceso = False
            return render_template('index2.html')
    elif request.method == 'GET':
        return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        if Acceso:
            frame = camera.get_frame()
            yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    if Acceso :
        return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
