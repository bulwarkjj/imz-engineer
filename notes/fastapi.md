# Notes, findings, and other related learned information for FastApi
## INDEX  
- Notes, findings, and other related learned information for FastApi
    - [Youtude learning video](#youtube-video)
    - [Run App Locally](#run-app-locally)
    - [URLS](#urls)
    - [PyDantic module](#pydantic-module)
    - [Jinja2Templates](#jinja2templates)
### Youtube video
- [Video URL](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- stopped at 1:02:32
### Run App Locally 
```uvicorn app.main:app --reload```  
- this will run the app in my linklocal address, great for debugging, seeing changes realtime. 
- ```uvicorn``` is a ASGI (_Async_ _Server_ _Gateway_ _Interface_) for webserver implementation
  - ```app.main:app``` is the path for my app named ```main``` from the dir ```app``` (app.main) which starts the FastApi object ```app``` in main.py
    - ```--reload``` is a flag that refreshs the link local page everytime I change ```main.py```

### URLS  
*this will change when I actually deploy, but for now they are my local favorites*
- [local url](http://127.0.0.1:8000)
- [Interactive docs](http://127.0.0.1:8000/docs)
- [alternative automatic documentation](http://127.0.0.1:8000/redoc)  

### PyDantic module
- I'm using the module ```pydantic`` in [main.py](/app/main.py) which does instant data validation for my endpoint which lifts some heavy work off my shoulders.  This done by typing hints and at runtime (using the swagger api interactive docs) it will provide intuitive error messages.  
  - pydantic comes with some helpful pre-built models like ```BaseModel``` and ```Field``` that I can use to easily create a page model for the app that includes things like field lengths, etc.

### Jinja2Templates
- this is a module for linking and using HTML pages for the app project
  - ```response_class=HTMLResponse``` allows the docs to know that the response will be HTML
  - you have to pass ```request``` as part of the key-value pairs in the context which means I will have to also declare it in my path operation. 
  - If I wanted to pass along context data i.e ```{id}```, I would use template-tagging format in my HTML pages i.e ```{{ id }}```
  - Still playing around with this, but so far I have been able to create a home page with a nav-bar (using bootstrap) in [main.py](../app/main.py)