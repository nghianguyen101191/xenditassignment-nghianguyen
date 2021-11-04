*Overview:
Python 3.8
Selenium
BDD: Behave
OCR: gpyocr (scan image to text - canas problems)
Design pattern: POM


*Evaluation criteria

1) Test scenario writing skills : positive, negative and boundary conditions:
- They are listed in detail in Feature File for automation test and GG Drive link
for manual Test
  - https://docs.google.com/spreadsheets/d/1vIoPQ2-_7ye_9IgS3me92TXXuKp9JOQAwZlcy9CaI4Q/edit?usp=sharing

2) Automation script generation : Usage of proper pass and fail conditions, report generation, screenshot capturing
- They are listed mainly in classes:
    + pages/calculate_page: actions on Calculate Page as POM
      
    + pages/util_page: control actions on page
      
    + utils/chrome_driver: Create Methods driver on Page
      
    + utils/manage_util: init Chrome Driver
      
    + utils/osr: define method to scan image and return text
    
    + tests/step_definitions/calculator_execution: Run all steps following BDD
    
    + tests/features/calculator_test.feature: feature file for BDD
*Environement:
      1) Install Python version > 2.7 and set up Interpreter :https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
      
      2) Install dependencies from Pipfile by:
  + pip install pipenv :  pip install pipenv
  
  + Tools: Use Pycharm (it is the best) or any others tools then install add-on to run python
  
  + Report: Allure with running command: 
   - brew install allure --> for Mac
   - scoop install allure --> win ( Refer link:https://docs.qameta.io/allure/)

* How to run

- Run all testcases: pipenv run behave

- Run with filter tags:
   + pipenv run behave --tags=<tag_name>
   + Eg: pipenv run behave --tags=functionaltest
- Reports
   + Run to generate report:  pipenv run open_report
   + Report Location: ./report folder





  