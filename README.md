## Notes App APIs using Django Rest-framework

### Apis List
  

#### Create  Note API 

    URL = http://localhost:8000/api/v1/createnote

    Data Format : 
    { 
        "title": "Note 1", 
       "body": "body of note 1"
    }



#### Get all Notes
    
    URL = http://localhost:8000/api/v1/getallnotes


#### Get Note By Id
     
     URL = http://localhost:8000/api/v1/getnotebyid/7a985056-d0e4-4539-bdc4-b2786fdd85b8


### Get Note By Title

    URL = http://localhost:8000/api/v1/getnotebytitle/?title=New Note2


###  Update a Note

    Method Type : PUT
    URL = http://localhost:8000/api/v1/updatenote/7a985056-d0e4-4539-bdc4-b2786fdd85b8

    Data Format : 
    {
        "title": "Title Updated3"
    }


    OR

    {
        "body": "Body Updated3"
    }

    OR 

    { 
        "title": "Updated Title", 
        "body" : "Updated Body"
    }



### Delete  A Note

    URL = http://localhost:8000/api/v1/deletenote/8f1e9295-ba5d-4a1f-9a0f-24fc4f491fb8
