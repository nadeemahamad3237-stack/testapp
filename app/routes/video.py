`
```python
from flask import Blueprint, request, jsonify
from .. import app
from ..models import video
from ..services import video as video_service

video_blueprint = Blueprint('video', __name__)

@video_blueprint.route('/video', methods=['POST'])
def create_video():
    data = request.get_json()
    video_service.create_video(data)
    return jsonify({'message': 'Video created successfully'}), 201
```

#