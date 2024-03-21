# Deploy locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

# Test with Android Client
Run this after launch emulator
```bash
# Remember to install platform-tools through Android Studio

cd "~\AppData\Local\Android\Sdk\platform-tools"

# Check if emulator is running
.\adb.exe devices

.\adb.exe reverse tcp:8000 tcp:8000
```

# Notes
## Swagger/API Documentation
```
http://localhost:8000/docs
```

## Differences between models and schemas
- /database/models: ORM classes/entity, references to database tables
- /database/schamas: Can be referenced to Response/Request Body model. This is use for API/Service Models.