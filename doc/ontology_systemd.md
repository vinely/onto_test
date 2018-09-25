# onotlogy setting systemd

## install the ontology

download right verion ontology

``` code
cp ontology /usr/local/bin
cd /root/
mkdir .ontology
chmod 600 .ontology
cd .ontology
echo ${mypassword} > ONTO_KEY
cp /path/to/config.json .
cp /path/to/wallet.dat .
cp /path/to/ontology.service /lib/systemd/system/
mkdir -p /var/lib/ontology
```

## start service

``` code
systemctl start ontology
```