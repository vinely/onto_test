# 1. Decentralized Identifiers (DIDs)

## 1.1 Overview

 Conventional **identity management** systems are based on centralized authorities such as corporate directory services, certificate authorities, or domain name registries. From the standpoint of cryptographic trust verification, each of these centralized authorities serves as its own root of trust. To make identity management work across these systems requires implementing federated identity management.

The emergence of distributed ledger technology (DLT), sometimes referred to as blockchain technology, provides the opportunity for fully decentralized identity management. In a **decentralized identity system**, entities are free to use any shared root of trust.

The entities are identified by **decentralized identifiers** (DIDs). They may authenticate via proofs (e.g., digital signatures, privacy-preserving biometric protocols, etc.). **DIDs** point to **DID Documents**. A DID Document contains a set of service endpoints for interacting with the entity.

To use a DID with a `particular distributed ledger or network` requires defining a **DID method** in a separate DID method specification. A DID method specifies the set of rules for how a DID is registered, resolved, updated, and revoked on that specific ledger or network.

Note that DID methods may also be developed for identifiers registered in federated or centralized identity management systems. For their part, all types of identifier systems may add support for DIDs. This creates an interoperability bridge between the worlds of centralized, federated, and decentralized identifiers.

## 1.2 The Generic DID

The generic DID scheme is a URI scheme conformant with [[RFC3986](https://tools.ietf.org/html/rfc3986)].

``` code
did = "did:" Method ":" Specific-idstring
```

URI reference with path and fragement:

``` code
         foo://example.com:8042/over/there?name=ferret#nose
         \_/   \______________/\_________/ \_________/ \__/
          |           |            |            |        |
       scheme     authority       path        query   fragment
          |   _____________________|__
         / \ /                        \
         urn:example:animal:ferret:nose
```

DID's reference is:

``` code
did-reference = did [ "/" did-path ][ "#" did-fragment ]
```

## 1.4 Registration DID Method

1. DID method specifications MUST include their own Security Considerations sections.
2. This section MUST consider all the requirements mentioned in section 5 of [[RFC3552](https://tools.ietf.org/html/rfc3552)] (page 27) for the DID operations defined in the specification.

This table summarizes the DID method specifications currently in development. The links will be updated as subsequent Implementer’s Drafts are produced.

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

## 1.4 Self-Managed DID Document

If a DID is the index key in a key-value pair, then the DID Document is the value to which the index key points. The combination of a DID and its associated DID Document forms the root record for a decentralized identifier.

A DID Document MUST be a single JSON object conforming to [[RFC7159](https://tools.ietf.org/html/rfc7159)]. For purposes of this version of the DID specification, the format of this [JSON](https://tools.ietf.org/html/rfc4627) object is specified in [JSON-LD](https://json-ld.org/), a format for mapping JSON data into the RDF semantic graph model as defined by [[JSON-LD](https://www.w3.org/DesignIssues/LinkedData.html)]. Future versions of this specification MAY specify other semantic graph formats for a DID Document such as JXD (JSON XDI Data), a serialization format for the [XDI graph model](http://docs.oasis-open.org/xdi/xdi-core/v1.0/csd01/xdi-core-v1.0-csd01.xml).

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

* `Context`

JSON objects in JSON-LD format must include a JSON-LD context statement. The rules for this statement are:

1.A DID Document MUST have exactly one top-level context statement.
2.The key for this property MUST be @context.
3.The value of this key MUST be the URL for the generic [DID context](https://w3id.org/did/v1.)

``` code
{
  "@context": "https://w3id.org/did/v1"
}
```

* `DID Subject`

The DID subject is the identifier that the DID Document is about, i.e., it is the DID described by DID Document. The rules for a DID subject are:

1.A DID Document MUST have exactly one DID subject.
2.The key for this property MUST be id.
3.The value of this key MUST be a valid DID.
4.When this DID Document is registered with the target distributed ledger or network, the registered DID MUST match this DID subject value.

``` code
{
  "id": "did:example:21tDAKCERh95uGgKbJNHYp"
}
```

* `Public Keys`

Public keys are used for digital signatures, encryption and other cryptographic operations, which in turn are the basis for purposes such as **authentication** or establishing secure communication with **service endpoints** . In addition, public keys may play a role in authorization mechanisms of **DID CRUD operations** This may be defined by DID Method specifications

The rules for public keys are:

1. A DID Document MAY include a publicKey property.
2. The value of the publicKey property should be an array of public keys.
3. Each public key must include id and type properties, and exactly one value property.
4. Each public key may include an owner property, which identifies the entity that controls the corresponding private key. If this property is missing, it is assumed to be the DID subject.
5. The value property of a public key may be publicKeyPem, publicKeyJwk, publicKeyHex, publicKeyBase64 or similar, depending on the format and encoding of the public key.

* `Authentication`
* `Authorization and Delegation`
* `Service Endpoints`
* `Created (Optional)`
* `Updated (Optional)`
* `Proof (Optional)`
* `Extensibility`

---------------------------------------------

## 2. ONT Identification Protocol Specification

**Ontology DID**(Also: **ONT ID**) is a decentralized identification protocol which based on W3C DID specifications.

The ONT ID is a decentralized identification protocol and it has the features of decentralization, self-management, privacy protection, security and ease of use. Each ONT ID corresponds to an **ONT ID Description Object** (DDO).

> The ONT ID protocol has been completely implemented by the smart contract of Ontology Blockchain. As a protocol layer, it follows a decoupled design, so it is not limited to Ontology Blockchain, but can also be implemented on other blockchains.

### 2.1 ONT As DID Method

1.Ontology DID Method Name
The namestring that shall identify this DID method is: `ont`.

A DID that uses this method **MUST** begin with the following prefix: `did:ont`. Per this DID specification, this string MUST be in lowercase.

2.Ontology DID Format
The decentralized identifiers(DID) on Ontology blockchain is of the following format:

``` code
ont-did   = "did:ont:" id-string
id-string = 1* idchar
idchar    = 1-9 / A-H / J-N / P-Z / a-k / m-z
```

`idchar` consists of all the characters in the base58 char set which is first defined by
Bitcoin. The Ontology DIDs are encoded using the base58 encoding method.

``` code
did:ont:AGsL32ZMvAwxYRN9Sv4mrgu3DgBSvTm5vt
```

### 2.1 ONT ID generation

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

### 2.2 Identity description object DDO specification (DID Document)

The DDO specification contains the following information:

* `PublicKeys`:The information of the public key used for identity authentication, including public key id, public key type, and public key data;

* `Attributes`:All attributes make up a JSON object;

* `Recovery`:The assigned restorer can help reset the user's public key list.'

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
