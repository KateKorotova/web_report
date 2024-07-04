## Racing Report Web Application with Flask

This is a Flask web application that generates and displays racing reports. The application includes multiple routes to display common statistics, a list of drivers, and detailed information about individual drivers. The data is read from provided files, ordered by lap time, and formatted for display.

## Usage
1. Install all required packages from requirement.txt:
```
pip install -r requirements.txt
```
2. Run the Flask application:
```
python run.py
```
3. Access the application in your web browser:
- Main report: http://localhost:9999/report/
- Drivers list: http://localhost:9999/report/drivers/
- Driver info: http://localhost:9999/report/drivers/?driver_id=DRIVER_ID
## Routes
**/report/**: Displays the main racing report with an optional order parameter to sort by lap time. E.g., **/report/?order=asc**.

**/report/drivers/**: Shows a list of driver names and codes. Each driver code is a link to detailed information about the driver.

**/report/drivers/?driver_id=DRIVER_ID**: Displays detailed information about the specified driver.
## Directory Structure
```
task-7-web-report-of-monaco-2018-racing/
│
├── app/
│   ├── __init__.py
│   ├── data/
│   │   ├── abbreviations.txt
│   │   ├── end.log
│   │   └── start.log
│   ├── templates/
│   │   ├── report.html
│   │   ├── drivers.html
│   │   └── driver_info.html
│   └── route.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── run.py
├── requirements.txt
└── README.md
```

## Roadmap

- change getting data from files to database 
- make prettier interface 

## Authors and acknowledgment
Author: Yekatierina Korotova