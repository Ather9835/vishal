import flask
from flask import request
from statsmodels.nonparametric.smoothers_lowess import lowess
from flask import jsonify

app = flask.Flask(__name__)


def findLocalMaximaMinima(n, arr):
    mn = []
    if arr[0] < arr[1]:
        mn.append(0)
    for i in range(1, n - 1):

        if arr[i - 1] > arr[i] < arr[i + 1]:
            mn.append(i)

    if arr[-1] < arr[-2]:
        mn.append(n - 1)
    return mn


def xx(arr):
    y_value = []
    x_value = []
    for i in arr:
        x_value.append(i[0])
        y_value.append(i[1])
    filtered = lowess(y_value, x_value, frac=0.05)
    minima_array_index = findLocalMaximaMinima(len(filtered[:, 1]), filtered[:, 1])
    print(minima_array_index)
    return minima_array_index


@app.route('/', methods=['GET'])
def home():
    appl = request.get_json()
    wave_int = appl["arr"]
    return jsonify(xx(wave_int))


if __name__ == '__main__':
    app.run()
