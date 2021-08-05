## git auth 

### storing the username and password 

The username and the password can be 

> stored in **cache** 

```bash
git config --global credential.helper cache --timeout=3600
```

## git changes handling 

### reverting all local changes 

all the local changes can be revered by 

```bash
git reset --hard
```

