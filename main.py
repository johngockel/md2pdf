import os
import tempfile
import pypandoc
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=["POST"])
def md2pdf():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    filepath = os.path.join(tempfile.gettempdir(), filename)
    uploaded_file.save(filepath)

    output_pdf = os.path.join(tempfile.gettempdir(), "output.pdf")
    pypandoc.convert_file(filepath, "pdf", outputfile=output_pdf)

    return send_file(output_pdf, mimetype="application/pdf")
