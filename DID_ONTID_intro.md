# Decentralized Identifiers (DIDs)

## 1. URIs, URLs, and URNs

URIs, URLs, and URNsDIDs have a foundation in URLs, so it's important to understand how the W3C clarified the terms [URI] (Uniform Resource Identifier), [URL] (Uniform Resource Locator), and [URN] (Uniform Resource Name) in September 2001.

## 2. The Generic DID

```code
did = "did:" method ":" specific-idstring
```

``` code
did-reference = did [ "/" did-path ][ "#" did-fragment ]
```

## 3. Registration DID Method

| Method Name  | Status      | DLT or Network    | Authors                                              | Link                                                         |
| ------------ | ----------- | ----------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| did:btcr:    | PROVISIONAL | Bitcoin           | Christopher Allen, Ryan Grant, Kim Hamilton Duffy    | [BTCR DID Method](https://w3c-ccg.github.io/didm-btcr)       |
| did:cnsnt:   | PROVISIONAL | Ethereum          | Consent                                              |                                                              |
| did:erc725:  | PROVISIONAL | Ethereum          | Markus Sabadello, Fabian Vogelsteller, Peter Kolarov | [erc725 DID Method](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/topics-and-advance-readings/DID-Method-erc725.md) |
| did:example: | PROVISIONAL | DID Specification | W3C Credentials Community Group                      | [DID Specification](https://w3c-ccg.github.io/did-spec/)     |
| did:ipid:    | PROVISIONAL | IPFS              | Jonathan Holt                                        |                                                              |
| did:sov:     | PROVISIONAL | Sovrin            | Mike Lodder                                          | [Sovrin DID Method](https://github.com/sovrin-foundation/sovrin/blob/master/spec/did-method-spec-template.html) |
| did:uport:   | PROVISIONAL | Ethereum          | uPort                                                |                                                              |
| did:v1:      | PROVISIONAL | Veres One         | Digital Bazaar                                       | [Veres One DID Method](https://w3c-ccg.github.io/didm-veres-one/) |
| did:dom:     | PROVISIONAL | Ethereum          | Dominode                                             |                                                              |
| did:ont:     | PROVISIONAL | Ontology          | Ontology Foundation                                  | [Ontology DID Method](https://github.com/ontio/ontology-DID/blob/master/docs/en/DID-ONT-method.md) |

## 4. Self-Managed DID Document

EXAMPLE : Minimal self-managed DID Document

``` json
{
    "@context": "https://w3id.org/did/v1",
    "id": "did:example:123456789abcdefghi",
    "publicKey": [{
        "id": "did:example:123456789abcdefghi#keys-1",
        "type": "RsaVerificationKey2018",
        "owner": "did:example:123456789abcdefghi",
        "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
    }],
    "authentication": [{
        // this key can be used to authenticate as DID ...9938
        "type": "RsaSignatureAuthentication2018",
        "publicKey": "did:example:123456789abcdefghi#keys-1"
    }],
    "service": [{
        "type": "ExampleService",
        "serviceEndpoint": "https://example.com/endpoint/8377464"
    }]
}
```

## ONT Identification Protocol Specification

### 1.1 ONT ID generation

1. `ripemd160`:hash160 32bytes temporary random nonce `20 bytes`
2. `sum with VER`: \<VER\> + data `VER is 0x41 in ont`
3. `add 4 byte checksum`:data + sha256sum(sha256sum(data))[:4] `25 bytes`
4. `base58`: bitcoin encode data
5. `did`: did:ont:\<data\> `SCHEME="did" METHOD="ont"`

ontology code:

``` go
func GenerateID() (string, error) {
    var buf [32]byte
    _, err := rand.Read(buf[:])
    if err != nil {
        return "", fmt.Errorf("generate ID error, %s", err)
    }
    return CreateID(buf[:])
}

func CreateID(nonce []byte) (string, error) {
    hasher := ripemd160.New()
    _, err := hasher.Write(nonce)
    if err != nil {
        return "", fmt.Errorf("create ID error, %s", err)
    }
    data := hasher.Sum([]byte{VER})
    data = append(data, checksum(data)...)

    bi := new(big.Int).SetBytes(data).String()
    idstring, err := base58.BitcoinEncoding.Encode([]byte(bi))
    if err != nil {
        return "", fmt.Errorf("create ID error, %s", err)
    }

    return SCHEME + ":" + METHOD + ":" + string(idstring), nil
}

func checksum(data []byte) []byte {
    sum := sha256.Sum256(data)
    sum = sha256.Sum256(sum[:])
    return sum[:4]
}
```

### 1.2 Identity description object DDO specification (DID Document)

The DDO specification contains the following information:

- `PublicKeys`：The information of the public key used for identity authentication, including public key id, public key type, and public key data;

- `Attributes`：All attributes make up a JSON object;

- `Recovery`：The assigned restorer can help reset the user's public key list.'

``` json
{
    "OntId": "did:ont:TVuF6FH1PskzWJAFhWAFg17NSitMDEBNoa",
    "Owners": [{
            "PubKeyId": "did:ont:TVuF6FH1PskzWJAFhWAFg17NSitMDEBNoa#keys-1",
            "Type": "ECDSA",
            "Curve": "nistp256",
            "Value":"022f71daef10803ece19f96b2cdb348d22bf7871c178b41f35a4f3772a8359b7d2"
        }, {
            "PublicKeyId": "did:ont:TVuF6FH1PskzWJAFhWAFg17NSitMDEBNoa#keys-2", 
            "Type": "RSA",
            "Length": 2048, 
            "Value": "3082010a...."
        }
    ],
    "Attributes": {
        "OfficialCredential": {
            "Service": "PKI",
            "CN": "ont.io",
            "CertFingerprint": "1028e8f7043f12c0c2069bd7c7b3b26213964566"
        }
    },
    "Recovery": "TA63T1gxXPXWsBqHtBKcV4NhFBhw3rtkAF"
}
```
