from chardet import detect
from flask import Flask, render_template, request, redirect, url_for
import subprocess



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create-data', methods=['POST'])
def create_data():
    user_id = request.form.get('userId')  # Get User ID from form
    if user_id:
        subprocess.run(["python", "datasetCreator.py", user_id])
        return '''
            <script>
                alert("Dataset creation completed for User ID: ''' + user_id + '''");
                window.location.href = '/';
            </script>
        '''
    return redirect(url_for('index'))

@app.route('/train')
def train():
    try:
        result = subprocess.run(["python", "trainer.py"], capture_output=True, text=True)
        log_output = result.stdout + "\n" + result.stderr
        print("Training Logs:\n", log_output)
    except Exception as e:
        log_output = f"Error: {str(e)}"
        print("Error:", str(e))  

    return render_template('train_complete.html', logs=log_output)


@app.route('/detect')
def detect_route():
    try:
        result = subprocess.run(["python", "detect.py"], capture_output=True, text=True)
        detected_persons = result.stdout.strip()
    except Exception as e:
        detected_persons = f"Error: {str(e)}"
    
    return render_template('index.html', detected_persons=detected_persons)


if __name__ == '__main__':
    app.run(debug=True, port=8542)
