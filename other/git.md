## git auth 

### storing the username and password 

The username and the password can be 

> stored in **cache** 

```bash
git config --global credential.helper cache --timeout=3600
```
## git configs 

### adding default editor 
The **VS code** can be added as default editor. 

```
git config --global core.editor " < VS Code file location > -w"

```
> note 
    VS code local file path => C:\Users\dinith.jayabodhi\AppData\Local\Programs\Microsoft VS Code\Code.exe

## git changes handling 

### reverting all local changes 

all the local changes can be revered by 

```bash
git reset --hard
```

## git clone 

### shallow clone 

``` bash 
git clone --depth 1 --branch <branch> --single-branch <repo-url>

```

- --depth - the history of the repo 
- --branch - the branches that should clone 

