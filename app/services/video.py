`
```python
from .. import db
from ..models import video

def create_video(data):
    new_video = video.Video(title=data['title'], content=data['content'])
    db.session.add(new_video)
    db.session.commit()
```

#