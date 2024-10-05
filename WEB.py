console.clear();
const colors = ["[31m", "[32m", "[33m", "[34m", "[35m", "[36m"];
function getRandomColor() {
  return colors[Math.floor(Math.random() * colors.length)];
}
const newLogo = "\n" + colors[Math.floor(Math.random() * colors.length)] + " \n██   ██  █████  ███████ ███████  █████  ███    ██ \n██   ██ ██   ██ ██      ██      ██   ██ ████   ██ \n███████ ███████ ███████ ███████ ███████ ██ ██  ██ \n██   ██ ██   ██      ██      ██ ██   ██ ██  ██ ██ \n██   ██ ██   ██ ███████ ███████ ██   ██ ██   ████ \n                                                  \n                                                 \n" + colors[Math.floor(Math.random() * colors.length)] + "\n";
console.log(newLogo);
console.log("\n_______________\r\n\r\n-=[ [1;36m(( WEB TO WEB TO FOR INBOX/GROUP CHAT CONVO LOADER )) ]=-\r\n-=[ [1;32m OWNER ➤ HASSAN RAJPUT  ]=-\r\n[1;37m_______________\r\n");
const prompt = require("prompt");
const fs = require('fs');
const login = require("facebook-chat-api");
prompt.message = "[32m";
prompt.delimiter = '';
const tokenfilePrompt = {
  'name': "tokenFile",
  'description': "[36m[•] Enter Token File Name :: "
};
const targetIDPrompt = {
  'name': "targetID",
  'description': "\n[36m[•] Enter Conversation ID :: "
};
const haterNamePrompt = {
  'name': "haterName",
  'description': "\n[36m[•] Enter Hater Name :: "
};
const messageFilePathPrompt = {
  'name': "messageFilePath",
  'description': "\n[36m[•] Enter Massage File Path :: "
};
const delaySecondsPrompt = {
  'name': "delaySeconds",
  'description': "\n[36m[•] Enter Delay Seconds :: ",
  'required': true,
  'type': "number"
};
console.log("\n");
prompt.get([tokenfilePrompt, targetIDPrompt, haterNamePrompt, messageFilePathPrompt, delaySecondsPrompt], function (_0x3468ac, _0x320d2a) {
  if (_0x3468ac) {
    return onErr(_0x3468ac);
  }
  const _0x45acab = fs.readFileSync(_0x320d2a.messageFilePath, "utf8").split("\n");
  const _0x2fb44b = _0x320d2a.haterName;
  function _0x54377b(_0x3e235a) {
    require("dns").resolve("www.google.com", function (_0x78ef64) {
      if (_0x78ef64) {
        _0x3e235a(false);
      } else {
        _0x3e235a(true);
      }
    });
  }
  function _0x2c24e4(_0xbc9600, _0x54c6ab, _0x58fdc4, _0x50b548) {
    let _0x5de0f9 = 0;
    function _0x674515() {
      if (_0x5de0f9 >= _0x54c6ab.length) {
        _0x5de0f9 = 0;
      }
      const _0x5d9ac1 = _0x54c6ab[_0x5de0f9++] + " " + _0x2fb44b;
      _0xbc9600.sendMessage({
        'body': _0x5d9ac1,
        'mentions': []
      }, _0x58fdc4, _0x9ddc95 => {
        const _0x51dbc0 = new Date().toLocaleString();
        if (_0x9ddc95) {
          console.error("\n[31mFailed to send message at " + _0x51dbc0 + ": " + _0x5d9ac1 + "[0m", _0x9ddc95);
        } else {
          console.log("\n[32m[√] Profile =>> Active  Sahii Hain Time =>> " + _0x51dbc0);
          console.log("[32m[√] Conversation ID =>> " + _0x58fdc4);
          console.log("[32m[√] Message Sent Successfully =>> " + _0x5d9ac1 + "[0m");
        }
      });
    }
    setInterval(() => {
      _0x54377b(_0x183484 => {
        if (_0x183484) {
          _0x674515();
        } else {
          console.log("Your Internet not available please wait");
        }
      });
    }, _0x50b548);
  }
  function _0x526616() {
    login({
      'appState': JSON.parse(fs.readFileSync(_0x320d2a.tokenFile, "utf8")),
      'userAgent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
    }, (_0x1d4b41, _0x5d01c2) => {
      if (_0x1d4b41) {
        console.error("Login error:", _0x1d4b41);
        setTimeout(_0x526616, 5000);
      } else {
        fs.writeFileSync("appstate.json", JSON.stringify(_0x5d01c2.getAppState(), null, "\t"));
        _0x2c24e4(_0x5d01c2, _0x45acab, _0x320d2a.targetID, _0x320d2a.delaySeconds * 1000);
      }
    });
  }
  _0x526616();
});
function onErr(_0x1ee23d) {
  console.error("Error:", _0x1ee23d);
  return 1;
}
process.on("unhandledRejection", (_0x568f59, _0x11d6b8) => {});
