## Task 2.1

```Wolfram
p = RandomPrime[{2^1023, 2^1024 - 1}];
q = RandomPrime[{2^1023, 2^1024 - 1}];

n = p*q;
phi = (p - 1)*(q - 1);

e = RandomPrime[{2^16, phi}];
While[GCD[e, phi] != 1, e = RandomPrime[{2^16, phi}]];

d = PowerMod[e, -1, phi];

message = ToCharacterCode["Zlatovcen Bogdan"];
encryptedMessage = PowerMod[message, e, n];

decryptedMessage = PowerMod[encryptedMessage, d, n];
decryptedText = FromCharacterCode[decryptedMessage];

Print["p value: ", p, "q value: ", q, "n value: ", n,
  "e value (public exponent): ", e,  "d value (private exponent): ",
  d, "Encrypted Message: ", encryptedMessage, "Decrypted Message: ",
  decryptedText];
```

## Task 2.2

```Wolfram
p = 323170060713110073001535134778251633624880571334890751745884341392\
6980683413621000279205636264016468545855635793533081692882902308057347\
2625273554742461245741026202527916572972862706300325263428213145766931\
4142236542209411113486299916574782680342305530863490506355577122191878\
9033272956969612974385624174123623722519734640269185579776797682301462\
5397933058015226858730761197532436467475855460715043896844940366130497\
6978128542959586595975670512838521327844685229255045682728791137200989\
3187395914337417583782600027803497319855206060753323412260325468408812\
0031105907484281003994966956119696956248629032338072839127039;
g = 2;
x = RandomInteger[{1, p - 2}];
y = PowerMod[g, x, p];

hexMessage = "5A 6C 61 74 6F 76 63 65 6E 20 42 6F 67 64 61 6E";
decimalMessage = ToExpression["16^^" <> #] & /@ StringSplit[hexMessage];

encrypt[message_, p_, g_, y_] := Module[{k, c1, c2},
  k = RandomInteger[{1, p - 2}];
  c1 = PowerMod[g, k, p];
  c2 = Mod[message*PowerMod[y, k, p], p];
  {c1, c2}
];

encryptedMessage = encrypt[#, p, g, y] & /@ decimalMessage;

decrypt[{c1_, c2_}, p_, x_] := Mod[c2*PowerMod[c1, p - 1 - x, p], p];

decryptedMessage = decrypt[#, p, x] & /@ encryptedMessage;

Print["Zlatovcen Bogdan in Decimal Form: ", decimalMessage, "Decrypted Message in Decimal Form: ", decryptedMessage, "Encrypted Message ", encryptedMessage];
```

## Task 2.3

```Wolfram
p = 3231700607131100730015351347782516336248805713348907517458843413926\
980683413621000279205636264016468545855635793533081692882902308057347\
262527355474246124574102620252791657297286270630032526342821314576693\
141422365422094111134862999165747826803423055308634905063555771221918\
789033272956969612974385624174123623722519734640269185579776797682301\
462539793305801522685873076119753243646747585546071504389684494036613\
049769781285429595865959756705128385213278446852292550456827287911372\
009893187395914337417583782600027803497319855206060753323412260325468\
4088120031105907484281003994966956119696956248629032338072839127039;
g = 2;

a = RandomInteger[{1, p - 1}];
b = RandomInteger[{1, p - 1}];
A = PowerMod[g, a, p];
B = PowerMod[g, b, p];

sharedSecretAlice = PowerMod[B, a, p];
sharedSecretBob = PowerMod[A, b, p];

Print["Alice's secret number: ", a, "Bob's secret number: ", b, "Alice's public key: ", A, "Bob's public key: ", B, "Shared secret computed by Alice: ", sharedSecretAlice, "Shared secret computed by Bob: ", sharedSecretBob];
```
