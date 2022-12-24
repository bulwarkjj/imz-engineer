# Notes, findings, and other related learned information for FastApi
## INDEX  
- [run app locally](#run-app-locally)  
- [URLs](#urls)
- [pydantic](#pydantic-module)

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