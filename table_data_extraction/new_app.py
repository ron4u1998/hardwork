from predict import PredictFunc
from PIL import Image
from app import TableData
import os
import cv2
import os
from flask import Flask, request, make_response, jsonify, send_file

app = Flask(__name__)


@app.route("/avai", methods=["GET", "POST"])
def final():
    try:
        folder_path = request.get_json()
    except Exception as e:
        return str(e)
    print(folder_path)
    for k, v in folder_path.items():
        for i in os.listdir(v):
            image_path = v + "/" + i
            obj = PredictFunc(image_path)
            result = obj.main_inf()
            try:
                x, y, w, h, s = result[0][0]
                img = Image.open(image_path)
                img2 = img.crop((x, y, w, h))
                img2.save(
                    "cropped"
                    + "/"
                    + image_path.split("/")[1].split(".")[0]
                    + "_cropped_out.png"
                )
                obj1 = TableData()
                x = obj1.table_data(
                    "cropped"
                    + "/"
                    + image_path.split("/")[1].split(".")[0]
                    + "_cropped_out.png"
                )
                print("hello")
                x.to_excel(
                    "xlsxfile" + "/" + image_path.split("/")[1].split(".")[0] + ".xlsx",
                    header=False,
                    index=False,
                )
            except Exception as e:
                print(e)
                print("NO TABLE DETECTED")
        return "done"


if __name__ == "__main__":
    app.run(port=2120, host="0.0.0.0", debug=True)

# x = final("rotated_fix/")
