### Open CV Applications

Updated for
* python 3.5.2
* opencv-python==3.4.1.15
* Django==2.0.5

#### Face Detector
##### Source: https://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/

Start the Django server:
```
python manage.py runserver
```
Then in another terminal run `api_testing.py`
```
python cv_api/face_detector/api_testing.py
```

It will detect the Obama's face.

##### Todo
- [x] Build the API.
- [x] Put into Django URL.
- [ ] Add some testcases.
- [ ] Make the app web-based with GUI.

#### Perspective Transform
source: https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
