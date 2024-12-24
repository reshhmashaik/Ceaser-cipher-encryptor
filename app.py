from flask import Flask, request, jsonify, render_template
import caesar_cipher

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar_cipher', methods=['POST'])
def encrypt_text():
    data = request.get_json()
    text = data['text']
    shift = data['shift']
    encrypted_text = caesar_cipher.caesar_cipher_encrypt(text, shift)
    return encrypted_text  # Return only the encrypted text

if __name__ == '__main__':
    app.run(debug=True)
