`
```python
from flask import request, jsonify
from . import app
from .ai import models
from .routes import video

@app.route('/')
def index():
    return 'TestApp'

if __name__ == '__main__':
    app.run(debug=True)
```

#