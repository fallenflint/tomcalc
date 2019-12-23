# Tom's retail calculator demo

## Quickstart

0. To run the demo, just open the [html doc](./app/calculator.html)
0. Tests are written using Selenium. You can run as follows:
   
    0. Create network first:
        
        `docker network create grid`

    0. Run test script:
        
        (it will take some time for the first time execution before you see tests running)
        `sh run_tests.sh`

Underneath it uses headless Chrome.
If you want to see live tests in a 'headed' Chrome session, just do next steps:

0. Install [selenium webdriver for Chrome](https://chromedriver.chromium.org/downloads) locally
1. Open test_calculator.py and replace line:

    `browser = webdriver.Chrome(options=chrome_options)`

    with line:
    
    `browser = webdriver.Chrome(<path_to_webdriver_executable>)`

    And line :
    
    `browser.get('file://./code/app/calculator.html')`
    
    with:
    
    `browser.get('file://<full_path_to_/calculator.html>')` 

    e.g:
    
    `browser.get('file://home/flint/projects/tomcalc/app/calculator.html')`