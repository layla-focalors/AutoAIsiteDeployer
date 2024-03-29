## Usage
push Html file is (deploy > index.html (Default))

```bash
├─deploy  
│  └─index.html  
├─modules  
│  ├─apis.py  
│  ├─deploy.py  
│  └─handler.py  
└─app.py  
```

## Command(ver.01.2)
```bash
# example
$ python apps.py -t fastapi -l DriveID:\DeployEngine\deploy -u https://github.com/layla-focalors/ds.git
```

## Command_Options
-t : Type of Deploy System
-l : Deploy Web Html File Path
-u : Your Web Files Git Repository URL
```