from flask  import Flask , render_template,request
from qr import QR
import io
import base64

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('website.html')
@app.route('/generate' , methods =['post'])
def generate():
    text=request.form.get('text_input')
    print(text)
    img=QR(text)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return render_template('website.html', qr_code=img_str)
    
    
    


if __name__ =="__main__":
    app.run(host='127.0.0.1',debug=True )

