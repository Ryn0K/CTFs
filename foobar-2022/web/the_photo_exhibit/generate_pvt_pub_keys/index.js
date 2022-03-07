const NodeRSA = require('node-rsa');

const KEY = new NodeRSA({b:512});
KEY.generateKeyPair();
pvt = KEY.exportKey('private');
pub = KEY.exportKey('public')
console.log(`private key : \n${pvt}`);
console.log(`public key : \n${pub}`)
n = KEY.exportKey('components-public').n.toString('base64');
console.log(`n: \n${n}`);