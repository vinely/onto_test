# onotlogy build

## ontology (ontology go sdk , ontology-eventbus, ontology-crypto)

### latest version

for version selection using glide

fix the glide.yml

``` glide.yml
package: github.com/ontio/ontology
import:
- package: github.com/ontio/ontology-eventbus
  version: v0.9.1
- package: github.com/ontio/ontology-crypto
  version: v1.0.2
- package: github.com/howeyc/gopass
- package: github.com/gorilla/websocket
  version: v1.2.0
- package: github.com/itchyny/base58-go
- package: github.com/pborman/uuid
  version: v1.1
- package: github.com/syndtr/goleveldb
  subpackages:
  - leveldb
  - leveldb/errors
  - leveldb/filter
  - leveldb/iterator
  - leveldb/opt
  - leveldb/util
- package: github.com/urfave/cli
  version: v1.20.0
- package: golang.org/x/text
  repo: https://github.com/golang/text.git
- package: golang.org/x/crypto
  repo: https://github.com/golang/crypto.git
  subpackages:
  - ripemd160
- package: github.com/hashicorp/golang-lru
- package: github.com/gosuri/uiprogress
- package: github.com/valyala/bytebufferpool
- package: github.com/stretchr/testify
- package: github.com/magiconair/properties
- package: golang.org/x/sys
  repo: https://github.com/golang/sys.git
  subpackages:
  - unix
ignore:
  - golang.org/x/sys/unix

```

- set $GOPATH to workspace
- glide up
- go build main.go 
  or using makefile like: make ontology-linux

### version v0.75

check out tag v0.75 ontology
fix the glide.yml

``` glide.yml
package: github.com/ontio/ontology
import:
- package: github.com/bitly/go-simplejson
  version: v0.5.0
- package: github.com/dnaproject/gopass
- package: github.com/gorilla/websocket
  version: v1.2.0
- package: github.com/itchyny/base58-go
- package: github.com/pborman/uuid
  version: v1.1
- package: github.com/syndtr/goleveldb
  subpackages:
  - leveldb
  - leveldb/errors
  - leveldb/filter
  - leveldb/iterator
  - leveldb/opt
  - leveldb/util
- package: github.com/urfave/cli
  version: v1.20.0
- package: github.com/orcaman/concurrent-map
- package: github.com/whyrusleeping/tar-utils
- package: golang.org/x/text
  repo: https://github.com/golang/text.git
- package: golang.org/x/crypto
  repo: https://github.com/golang/crypto.git
  subpackages:
  - ripemd160
- package: github.com/Workiva/go-datastructures
- package: github.com/AsynkronIT/goconsole
- package: golang.org/x/sys
  repo: https://github.com/golang/sys.git
  subpackages:
  - unix
  - windows
- package: golang.org/x/net
  repo: https://github.com/golang/net.git
  subpackages:
  - context
- package: google.golang.org/grpc
  repo: https://github.com/grpc/grpc-go.git
- package: github.com/hashicorp/golang-lru
- package: github.com/ontio/ontology-go-sdk
  version: 80dcfae123b03d6cbbc630e504189fc50eb2937e
- package: google.golang.org/genproto
  repo: https://github.com/google/go-genproto.git
- package: github.com/ontio/ontology-crypto
  version: v0.9
- package: github.com/ontio/ontology-eventbus
  version: v0.9  
ignore:
  - golang.org/x/sys/unix

```

- set $GOPATH to workspace
- glide up
- go build main.go

## ontology java sdk

maven build