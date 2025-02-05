from flask import Flask, request, jsonify, send_file
import io
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>TTF to WOFF2 Converter</title>
    </head>
    <body>
        <h1>TTF to WOFF2 Converter</h1>
        <form action="/convert" method="post" enctype="multipart/form-data">
            <label for="ttfFile">Upload TTF file:</label>
            <input type="file" id="ttfFile" name="ttfFile" accept=".ttf" required>
            <button type="submit">Convert</button>
        </form>
    </body>
    </html>
    '''

@app.route('/convert', methods=['POST'])
def upload_file():
    if 'ttfFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['ttfFile']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not file.filename.endswith('.ttf'):
        return jsonify({'error': 'File is not a TTF font'}), 400

    # Read the TTF file into memory
    ttf_data = io.BytesIO(file.read())

    # Convert TTF to WOFF2 in memory
    try:
        # Load the font
        font = TTFont(ttf_data)

        # Subsetting options
        options = Options()
        options.flavor = 'woff2'
        options.layout_features = [
            'tnum', 'ss01', 'ss02', 'ss03', 'ss04', 'ss05', 'ss06', 'ss07', 'ss08', 'ss09', 
            'ss10', 'ss11', 'ss12', 'ss13', 'ss14', 'ss15'
        ]
        options.unicodes = (
            list(range(0x0020, 0x0080)) +
            list(range(0x0080, 0x0100)) +
            [0x201E, 0x201C, 0x20AC, 0x201C, 0x201D, 0x2013, 0x2014, 0x2212, 0x2002, 0x2003]
        )

        # Subsetting the font
        subsetter = Subsetter(options=options)
        subsetter.populate(unicodes=options.unicodes)
        subsetter.subset(font)

        # Save the subsetted font to WOFF2
        woff2_data = io.BytesIO()
        font.flavor = 'woff2'
        font.save(woff2_data)
        woff2_data.seek(0)

        # Send the WOFF2 file as a response
        return send_file(woff2_data, mimetype='font/woff2', as_attachment=True, download_name=file.filename.replace('.ttf', '.woff2'))

    except Exception as e:
        return jsonify({'error': 'Conversion failed', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
