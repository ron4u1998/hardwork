FROM python:3.8

#update packages
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install --upgrade pip

#install required libraries for some libraries
RUN pip install pyocr
RUN pip install cython
RUN pip install numpy
RUN pip install opencv-python
RUN pip install torchvision
RUN apt-get -y install python3-dev
RUN apt -y install python3-tk

#install required libraries for model
RUN pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI

#install tools for ocr and pdf2image
RUN apt-get -y install tesseract-ocr
RUN apt-get install tesseract-ocr-eng
RUN apt-get -y install poppler-utils

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN pip install torch==1.13.0

RUN pip install git+https://github.com/facebookresearch/detectron2.git

RUN pip install mmcv-full==1.7.0 -f https://download.openmmlab.com/mmcv/dist/cpu/torch1.13/index.html

RUN pip install -r requirements.txt

RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1WTwpJbZz1jrQNU5zwe9j4wQ9JbZr9zXi' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1WTwpJbZz1jrQNU5zwe9j4wQ9JbZr9zXi" -O /app/description.pth && rm -rf /tmp/cookies.txt

RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1iJTkS0H-whcEAS8UWRspVU-R8lh67S1s' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1iJTkS0H-whcEAS8UWRspVU-R8lh67S1s" -O /app/model/layoutlmv2_sam_ocr.pth && rm -rf /tmp/cookies.txt

COPY xml_flie/paddleocr.py /usr/local/lib/python3.8/site-packages/paddleocr/paddleocr.py

CMD ["python" , "app.py"]
