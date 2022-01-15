# UUID API Docker
A simple API to return key-value pair of randomly generated UUID. Built with Docker, Django, and MySQL.  
Key will be the timestamp while value is the UUID. The API returns all previous UUID ever generated by the API.  
**Example**
>{
>"2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"
>"2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",
>"2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",
>}

## Requirements
- Docker
- docker-compose
## installation
1. Build Docker backend.   
```docker-compose up --build ```  
This only applies to inital run. Subsequent runs should use ```docker-compose up```
2. Migrate tables in backend. While services are running, in another terminal type:  
```docker-compose exec backend sh```  
to enter the backend service.  
3. Run Django migrate command:   
```python manage.py migrate```  
4. Access API at ```http://0.0.0.0:8000/api/uuid```


## Usage
1. Start Django and MySQL services:  
```docker-compose up```

## Support
- Need help contact [ME](mailto:akandevic@gmail.com?subject=Support:UUID-API)
- Access django backend with:  
```docker-compose exec backend sh```