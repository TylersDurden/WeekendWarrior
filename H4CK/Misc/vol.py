foundAES = False
foundB64 = False
try:
    import os
except ImportError:
    hasOS = False
    pass
try:
    import base64
    foundB64 = True
except ImportError:
    pass
try:
    from Crypto.Cipher import AES
    foundAES = True
except ImportError:
    pass
''' END OF IMPORTs '''
# ====================================UTIL_FCNs========================================== #


def swap(fname,destroy):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def file_encrypt(fname, destroy):
    BSZ = 16
    PADDING = '{'
    # DEFINE PADDING FUNCTION
    PAD = lambda s: s + (BSZ - len(s) % BSZ) * PADDING
    # EXTRACT FILE's CLEAR_TEXT
    content = ''
    for element in open(fname, 'r').readlines():
        content += element
    if destroy:
        os.remove(fname)
    # GET SOME RANDOM BYTES AND ENCRYPT
    secret = os.urandom(BSZ)
    if foundAES and foundB64:
        c = AES.new(secret)
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(PAD(s)))
        encrypted_data = EncodeAES(c, content)
        open('enc.txt', 'w').write(encrypted_data)
    return secret


def file_decrypt(fname, destroy, key):
    PADDING = '{'
    # EXTRACT FILE's CLEAR_TEXT
    content = ''
    for element in open(fname, 'r').readlines():
        if element.split(' ')[0] == '\n ':
            content += element
        else:
            content += element + ' '
    if destroy:
        os.remove(fname)
    if foundAES and foundB64:
        c = AES.new(key)
        DecodeAES = lambda c, s: c.decrypt(base64.b64decode(s)).rstrip(PADDING)
        return DecodeAES(c, content)

# ======================================================================================= #


prog = 's3c.py'
key = file_encrypt(prog, True)
clear_prog = file_decrypt('enc.txt', True, key)
ln1 = clear_prog.split('\n')[0]
rest = clear_prog.split(ln1)[1:]

os.system('ls; sleep 3')
print 'Creating Program from encrypted BLOB'
open('program.py','w').write(clear_prog)
print 'Attempting to run decrypted program'
os.system('python program.py run')
os.system('rm program.py')
print '===================== FINISHED ======================'
