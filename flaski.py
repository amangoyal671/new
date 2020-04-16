from flask import Flask
from flask import request
from flask import jsonify
import apk_download   #apkdownload script
import andro #(androguard)
import ml_algo

app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
	if request.method == 'POST':
		packagename = request.form['packageName']
		apk_download.download_apk(packagename)
		andro.mainn()
		output = ml_algo.tree()
		return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)