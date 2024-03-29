import hashlib

def sha1_for_largefile(filepath, blocksize=8192):
    sha_1 = hashlib.sha1()
    filepath = filepath + '/index.html'
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha_1.update(buf)
    # return sha_1.hexdigest()
    return {'Hash': sha_1.hexdigest(), 'Status': 'Success'}
