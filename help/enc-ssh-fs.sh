# Unmount
fusermount -u ~/attic
fusermount -u ~/.atticssh-encfsdump

#mount
sshfs attic:/home/tim/ENCFSDUMP ~/.atticssh-encfsdump
encfs ~/.atticssh-encfsdump ~/.atticssh-encfsdump

## Create Options
# AES 256 4096 block

# For a temp shell with it mounted..
encfs ~/.atticssh-encfsdump ~/.atticssh-encfsdump


