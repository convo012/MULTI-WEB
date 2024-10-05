const axios = require("axios");
const os = require('os');
const crypto = require("crypto");
const https = require("https");
const readline = require("readline");
const {
  exec
} = require("child_process");
console.clear();
console.log("[1;33m----------------------------------------------");
console.log("[32mImportant Note");
console.log("[1;33m----------------------------------------------");
console.log("[32m╔══════════════════════╗");
console.log("[32m║╔════════════════════╗╚╗");
console.log("[32m║║██░░░░░░░░░░░░░░░░░░╚╗╚╗");
console.log("[32m║║██░░░HASSAN RAJPUT ░░░░ ─║║║");
console.log("[32m║║██░░░░░░░░░░░░░░░░░░╔╝╔╝");
console.log("[32m║╚════════════════════╝╔╝");
console.log("[32m╚══════════════════════╝");
console.log("[32m---------------------------------------------------");
console.log("[33m𝗧𝗢𝗢𝗟𝗦 𝗨𝗣𝗗𝗔𝗧𝗘 𝗙𝗜𝗥𝗦𝗧 𝗦𝗘𝗡𝗧 𝗙𝗥𝗜𝗘𝗡𝗗 𝗥𝗘𝗤𝗨𝗘𝗦𝗧 ");
console.log("[32m---------------------------------------------------");
console.log("[32m[+] 𝗔𝗨𝗧𝗛𝗢𝗥=>     HASSAN RAJPUT");
console.log("[33m[+] 𝗧𝗘𝗔𝗠=>      ONE MAN ARMY");
console.log("[32m[+] 𝗩𝗘𝗥𝗦𝗜𝗢𝗡=>  :0.1");
console.log("[33m--------------------------------------");
console.log("[1;33mMulti Ids Web To Web Convo");
console.log("[1;33mALL HATERS FUCK YOU BITCH");
console.log("[1;33mMonthly Subscription Price Rs :500");
console.log("[1;33mFR33 K4 T00L SAMJL3 JHATU");
console.log("[32mYour Key is not approved");
console.log("[1;33m----------------------------------------------");
console.log("[32mYou Have to Take Approval first");
console.log("[1;33m----------------------------------------------");
const uniqueKey = crypto.createHash("sha256").update(os.userInfo().uid.toString() + os.userInfo().username).digest("hex");
console.log("[32mYour Key:", uniqueKey);
console.log("[1;33m----------------------------------------------");
checkPermission(uniqueKey);
function getUniqueId() {
  return crypto.createHash("sha256").update(os.userInfo().uid.toString() + os.userInfo().username).digest("hex");
}
function checkPermission(_0x171d4c) {
  axios.get("https://github.com/convo012/APROVAL/blob/main/multy-web.txt").then(_0x4e04e9 => {
    let _0x14f86f = _0x4e04e9.data;
    let _0x498195 = _0x14f86f.split("\n").map(_0x26fc08 => _0x26fc08.trim()).filter(_0x19e335 => _0x19e335.includes(_0x171d4c));
    if (_0x498195.length === 0) {
      console.log("[31mSorry, you don't have permission to run this script.");
      sendApprovalRequest(_0x171d4c);
    } else {
      console.log("[32mPermission granted. You can proceed with the script.");
      console.log("\n[1;36m$$   $$  $$$$$$   $$$$$$   $$$$$$   $$$$$$  $$   $$ ");
      console.log("\n[1;36m$$ |  $$ |$$  __$$ $$  __$$ $$  __$$ $$  __$$ $$$  $$ |   ");
      console.log("\n[1;36m$$ |  $$ |$$ /  $$ |$$ /  __|$$ /  __|$$ /  $$ |$$$$ $$ | ");
      console.log("\n[1;36m$$$$$$$$ |$$$$$$$$ |$$$$$$  $$$$$$  $$$$$$$$ |$$ $$$$ | ");
      console.log("\n[1;36m$$  __$$ |$$  __$$ | ____$$  ____$$ $$  __$$ |$$ $$$$ | ");
      console.log("\n[1;36m$$ |  $$ |$$ |  $$ |$$   $$ |$$   $$ |$$ |  $$ |$$ |$$$ | ");
      console.log("\n[1;36m$$ |  $$ |$$ |  $$ |$$$$$$  |$$$$$$  |$$ |  $$ |$$ | $$ | ");
      console.log("\n[1;36m__|  __|__|  __| ______/  ______/ __|  __|__|  __| ");
      console.clear();
      console.log("[33m%s[0m", '');
      const _0x2fcea4 = require("prompt");
      const _0x489a5f = require('fs');
      const _0x34fde2 = require("fca-unofficial");
      const _0x37186f = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"];
      const _0x1c28ba = new https.Agent({
        'rejectUnauthorized': false
      });
      _0x2fcea4.start();
      _0x2fcea4.get(["IdNAME", "IdNAME2", "IdNAME3", "IdNAME4", "IdNAME5", "IdNAME6", "IdNAME7", "IdNAME8"], function (_0x4a1cf1, _0x3f4449) {
        if (_0x4a1cf1) {
          return _0x461ff0(_0x4a1cf1);
        }
        _0xde74c8('', _0x3f4449);
      });
      function _0xde74c8(_0x35b66b, _0x10a904) {
        let _0x101485 = [JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME2 || '' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME3 || '' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME4 || '' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME5 || '' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME6 || '' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME7 || '' + _0x10a904.IdNAME, "utf8")), JSON.parse(_0x489a5f.readFileSync('' + _0x10a904.IdNAME8 || '' + _0x10a904.IdNAME, "utf8"))];
        let _0x1d6a11 = [];
        _0x101485.forEach((_0x133841, _0x112bc8) => {
          !function _0x26c0d4(_0x806d61, _0x398477) {
            _0x34fde2({
              'appState': _0x806d61,
              'userAgent': _0x37186f[_0x398477],
              'forceLogin': true,
              'httpOptions': {
                'agent': _0x1c28ba
              }
            }, (_0x394337, _0x2ffc54) => {
              if (_0x394337) {
                console.log("Error logging in with account " + (_0x398477 + 1) + ", retrying...");
                _0x26c0d4(_0x806d61, _0x398477);
              } else {
                _0x1d6a11[_0x398477] = _0x2ffc54;
              }
            });
          }(_0x133841, _0x112bc8);
        });
        let _0x453d53 = 0;
        _0x2fcea4.get(["Select20targetIDs"], function (_0x3fd4cc, _0x2d93e3) {
          if (_0x3fd4cc) {
            return _0x461ff0(_0x3fd4cc);
          }
          switch (_0x2d93e3.Select20targetIDs) {
            case '1':
              _0x2fcea4.get(["targetID", "short", "file", "timer"], function (_0x467110, _0x493c08) {
                if (_0x467110) {
                  return _0x461ff0(_0x467110);
                }
                let _0x53bca7 = _0x489a5f.readFileSync(_0x493c08.file, "utf8").split("\n").filter(Boolean);
                let _0xb93ae7 = 0;
                setInterval(() => {
                  let _0x1096f0 = _0x493c08.short + _0x53bca7[_0xb93ae7];
                  _0x1d6a11[_0x453d53].sendMessage(_0x1096f0, _0x493c08.targetID, () => {});
                  if (++_0xb93ae7 >= _0x53bca7.length) {
                    _0xb93ae7 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x493c08.timer + "000");
              });
              break;
            case '2':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "timer"], function (_0xaff943, _0x5963cd) {
                if (_0xaff943) {
                  return _0x461ff0(_0xaff943);
                }
                let _0x32600c = _0x489a5f.readFileSync(_0x5963cd.file1, "utf8").split("\n").filter(Boolean);
                let _0x568f33 = _0x489a5f.readFileSync(_0x5963cd.file2, "utf8").split("\n").filter(Boolean);
                let _0x391ccd = 0;
                let _0x10a6a1 = 0;
                setInterval(() => {
                  let _0xa97b05 = _0x5963cd.short + _0x32600c[_0x391ccd];
                  let _0x9c6ec5 = _0x5963cd.short2 + _0x568f33[_0x10a6a1];
                  _0x1d6a11[_0x453d53].sendMessage(_0xa97b05, _0x5963cd.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x9c6ec5, _0x5963cd.targetID2, () => {});
                  _0x391ccd++;
                  _0x10a6a1++;
                  if (_0x391ccd >= _0x32600c.length) {
                    _0x391ccd = 0;
                  }
                  if (_0x10a6a1 >= _0x568f33.length) {
                    _0x10a6a1 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x5963cd.timer + "000");
              });
              break;
            case '3':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "timer"], function (_0x50797c, _0x5a5d74) {
                if (_0x50797c) {
                  return _0x461ff0(_0x50797c);
                }
                let _0x3e637f = _0x489a5f.readFileSync(_0x5a5d74.file1, "utf8").split("\n").filter(Boolean);
                let _0x13e8e9 = _0x489a5f.readFileSync(_0x5a5d74.file2, "utf8").split("\n").filter(Boolean);
                let _0x2d9f14 = _0x489a5f.readFileSync(_0x5a5d74.file3, "utf8").split("\n").filter(Boolean);
                let _0x313518 = 0;
                let _0x490d09 = 0;
                let _0x4ebb3e = 0;
                setInterval(() => {
                  let _0x590868 = _0x5a5d74.short + _0x3e637f[_0x313518];
                  let _0x186802 = _0x5a5d74.short2 + _0x13e8e9[_0x490d09];
                  let _0x297462 = _0x5a5d74.short3 + _0x2d9f14[_0x4ebb3e];
                  _0x1d6a11[_0x453d53].sendMessage(_0x590868, _0x5a5d74.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x186802, _0x5a5d74.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x297462, _0x5a5d74.targetID3, () => {});
                  _0x313518++;
                  _0x490d09++;
                  _0x4ebb3e++;
                  if (_0x313518 >= _0x3e637f.length) {
                    _0x313518 = 0;
                  }
                  if (_0x490d09 >= _0x13e8e9.length) {
                    _0x490d09 = 0;
                  }
                  if (_0x4ebb3e >= _0x2d9f14.length) {
                    _0x4ebb3e = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x5a5d74.timer + "000");
              });
              break;
            case '4':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "timer"], function (_0xa2e792, _0x227196) {
                if (_0xa2e792) {
                  return _0x461ff0(_0xa2e792);
                }
                let _0x3b652f = _0x489a5f.readFileSync(_0x227196.file1, "utf8").split("\n").filter(Boolean);
                let _0x491c64 = _0x489a5f.readFileSync(_0x227196.file2, "utf8").split("\n").filter(Boolean);
                let _0x16970f = _0x489a5f.readFileSync(_0x227196.file3, "utf8").split("\n").filter(Boolean);
                let _0x449e10 = _0x489a5f.readFileSync(_0x227196.file4, "utf8").split("\n").filter(Boolean);
                let _0x2918a9 = 0;
                let _0x5aff0d = 0;
                let _0x53c683 = 0;
                let _0x280198 = 0;
                setInterval(() => {
                  let _0x1c545e = _0x227196.short + _0x3b652f[_0x2918a9];
                  let _0x5b0d28 = _0x227196.short2 + _0x491c64[_0x5aff0d];
                  let _0x5de42b = _0x227196.short3 + _0x16970f[_0x53c683];
                  let _0x3d37a1 = _0x227196.short4 + _0x449e10[_0x280198];
                  _0x1d6a11[_0x453d53].sendMessage(_0x1c545e, _0x227196.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5b0d28, _0x227196.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5de42b, _0x227196.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3d37a1, _0x227196.targetID4, () => {});
                  _0x2918a9++;
                  _0x5aff0d++;
                  _0x53c683++;
                  _0x280198++;
                  if (_0x2918a9 >= _0x3b652f.length) {
                    _0x2918a9 = 0;
                  }
                  if (_0x5aff0d >= _0x491c64.length) {
                    _0x5aff0d = 0;
                  }
                  if (_0x53c683 >= _0x16970f.length) {
                    _0x53c683 = 0;
                  }
                  if (_0x280198 >= _0x449e10.length) {
                    _0x280198 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x227196.timer + "000");
              });
              break;
            case '5':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "timer"], function (_0x2dc1b8, _0x512bb7) {
                if (_0x2dc1b8) {
                  return _0x461ff0(_0x2dc1b8);
                }
                let _0x88900c = _0x489a5f.readFileSync(_0x512bb7.file1, "utf8").split("\n").filter(Boolean);
                let _0x7e21ce = _0x489a5f.readFileSync(_0x512bb7.file2, "utf8").split("\n").filter(Boolean);
                let _0x130c19 = _0x489a5f.readFileSync(_0x512bb7.file3, "utf8").split("\n").filter(Boolean);
                let _0x4e29c9 = _0x489a5f.readFileSync(_0x512bb7.file4, "utf8").split("\n").filter(Boolean);
                let _0x1b8c86 = _0x489a5f.readFileSync(_0x512bb7.file5, "utf8").split("\n").filter(Boolean);
                let _0xd18c18 = 0;
                let _0x56d049 = 0;
                let _0x225565 = 0;
                let _0x552f2b = 0;
                let _0x59a4dc = 0;
                setInterval(() => {
                  let _0x10458f = _0x512bb7.short + _0x88900c[_0xd18c18];
                  let _0x903824 = _0x512bb7.short2 + _0x7e21ce[_0x56d049];
                  let _0x55657a = _0x512bb7.short3 + _0x130c19[_0x225565];
                  let _0xc89c64 = _0x512bb7.short4 + _0x4e29c9[_0x552f2b];
                  let _0x7f5fde = _0x512bb7.short5 + _0x1b8c86[_0x59a4dc];
                  _0x1d6a11[_0x453d53].sendMessage(_0x10458f, _0x512bb7.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x903824, _0x512bb7.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x55657a, _0x512bb7.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xc89c64, _0x512bb7.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x7f5fde, _0x512bb7.targetID5, () => {});
                  _0xd18c18++;
                  _0x56d049++;
                  _0x225565++;
                  _0x552f2b++;
                  _0x59a4dc++;
                  if (_0xd18c18 >= _0x88900c.length) {
                    _0xd18c18 = 0;
                  }
                  if (_0x56d049 >= _0x7e21ce.length) {
                    _0x56d049 = 0;
                  }
                  if (_0x225565 >= _0x130c19.length) {
                    _0x225565 = 0;
                  }
                  if (_0x552f2b >= _0x4e29c9.length) {
                    _0x552f2b = 0;
                  }
                  if (_0x59a4dc >= _0x1b8c86.length) {
                    _0x59a4dc = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x512bb7.timer + "000");
              });
              break;
            case '6':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "timer"], function (_0x307f21, _0x1db633) {
                if (_0x307f21) {
                  return _0x461ff0(_0x307f21);
                }
                let _0x127509 = _0x489a5f.readFileSync(_0x1db633.file1, "utf8").split("\n").filter(Boolean);
                let _0x3d9897 = _0x489a5f.readFileSync(_0x1db633.file2, "utf8").split("\n").filter(Boolean);
                let _0x4fc188 = _0x489a5f.readFileSync(_0x1db633.file3, "utf8").split("\n").filter(Boolean);
                let _0x2a20b2 = _0x489a5f.readFileSync(_0x1db633.file4, "utf8").split("\n").filter(Boolean);
                let _0x42ab4b = _0x489a5f.readFileSync(_0x1db633.file5, "utf8").split("\n").filter(Boolean);
                let _0xf8960c = _0x489a5f.readFileSync(_0x1db633.file6, "utf8").split("\n").filter(Boolean);
                let _0x5b0e0f = 0;
                let _0x1faf1d = 0;
                let _0x2c8cae = 0;
                let _0x4b9748 = 0;
                let _0x3b5690 = 0;
                let _0x2edce = 0;
                setInterval(() => {
                  let _0x3e6633 = _0x1db633.short + _0x127509[_0x5b0e0f];
                  let _0x14808b = _0x1db633.short2 + _0x3d9897[_0x1faf1d];
                  let _0x194f0b = _0x1db633.short3 + _0x4fc188[_0x2c8cae];
                  let _0x3bfbae = _0x1db633.short4 + _0x2a20b2[_0x4b9748];
                  let _0x45e361 = _0x1db633.short5 + _0x42ab4b[_0x3b5690];
                  let _0x342996 = _0x1db633.short6 + _0xf8960c[_0x2edce];
                  _0x1d6a11[_0x453d53].sendMessage(_0x3e6633, _0x1db633.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x14808b, _0x1db633.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x194f0b, _0x1db633.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3bfbae, _0x1db633.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x45e361, _0x1db633.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x342996, _0x1db633.targetID6, () => {});
                  _0x5b0e0f++;
                  _0x1faf1d++;
                  _0x2c8cae++;
                  _0x4b9748++;
                  _0x3b5690++;
                  _0x2edce++;
                  if (_0x5b0e0f >= _0x127509.length) {
                    _0x5b0e0f = 0;
                  }
                  if (_0x1faf1d >= _0x3d9897.length) {
                    _0x1faf1d = 0;
                  }
                  if (_0x2c8cae >= _0x4fc188.length) {
                    _0x2c8cae = 0;
                  }
                  if (_0x4b9748 >= _0x2a20b2.length) {
                    _0x4b9748 = 0;
                  }
                  if (_0x3b5690 >= _0x42ab4b.length) {
                    _0x3b5690 = 0;
                  }
                  if (_0x2edce >= _0xf8960c.length) {
                    _0x2edce = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x1db633.timer + "000");
              });
              break;
            case '7':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "timer"], function (_0x24b6b2, _0x44b441) {
                if (_0x24b6b2) {
                  return _0x461ff0(_0x24b6b2);
                }
                let _0x23388c = _0x489a5f.readFileSync(_0x44b441.file1, "utf8").split("\n").filter(Boolean);
                let _0x291edd = _0x489a5f.readFileSync(_0x44b441.file2, "utf8").split("\n").filter(Boolean);
                let _0x190969 = _0x489a5f.readFileSync(_0x44b441.file3, "utf8").split("\n").filter(Boolean);
                let _0x30d9cd = _0x489a5f.readFileSync(_0x44b441.file4, "utf8").split("\n").filter(Boolean);
                let _0x5d9a30 = _0x489a5f.readFileSync(_0x44b441.file5, "utf8").split("\n").filter(Boolean);
                let _0x26fe67 = _0x489a5f.readFileSync(_0x44b441.file6, "utf8").split("\n").filter(Boolean);
                let _0x115936 = _0x489a5f.readFileSync(_0x44b441.file7, "utf8").split("\n").filter(Boolean);
                let _0x4bf3a1 = 0;
                let _0x2b0fed = 0;
                let _0x459cf8 = 0;
                let _0x567161 = 0;
                let _0x2307d1 = 0;
                let _0x405a49 = 0;
                let _0x4970b8 = 0;
                setInterval(() => {
                  let _0x2fa1c5 = _0x44b441.short + _0x23388c[_0x4bf3a1];
                  let _0x115df4 = _0x44b441.short2 + _0x291edd[_0x2b0fed];
                  let _0x22b6a2 = _0x44b441.short3 + _0x190969[_0x459cf8];
                  let _0x7722cb = _0x44b441.short4 + _0x30d9cd[_0x567161];
                  let _0x495707 = _0x44b441.short5 + _0x5d9a30[_0x2307d1];
                  let _0x249f5c = _0x44b441.short6 + _0x26fe67[_0x405a49];
                  let _0x123f73 = _0x44b441.short7 + _0x26fe67[_0x405a49];
                  _0x1d6a11[_0x453d53].sendMessage(_0x2fa1c5, _0x44b441.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x115df4, _0x44b441.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x22b6a2, _0x44b441.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x7722cb, _0x44b441.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x495707, _0x44b441.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x249f5c, _0x44b441.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x123f73, _0x44b441.targetID7, () => {});
                  _0x4bf3a1++;
                  _0x2b0fed++;
                  _0x459cf8++;
                  _0x567161++;
                  _0x2307d1++;
                  _0x405a49++;
                  _0x4970b8++;
                  if (_0x4bf3a1 >= _0x23388c.length) {
                    _0x4bf3a1 = 0;
                  }
                  if (_0x2b0fed >= _0x291edd.length) {
                    _0x2b0fed = 0;
                  }
                  if (_0x459cf8 >= _0x190969.length) {
                    _0x459cf8 = 0;
                  }
                  if (_0x567161 >= _0x30d9cd.length) {
                    _0x567161 = 0;
                  }
                  if (_0x2307d1 >= _0x5d9a30.length) {
                    _0x2307d1 = 0;
                  }
                  if (_0x405a49 >= _0x26fe67.length) {
                    _0x405a49 = 0;
                  }
                  if (_0x4970b8 >= _0x115936.length) {
                    _0x4970b8 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x44b441.timer + "000");
              });
              break;
            case '8':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "timer"], function (_0x128cc2, _0x30190a) {
                if (_0x128cc2) {
                  return _0x461ff0(_0x128cc2);
                }
                let _0x4d8d56 = _0x489a5f.readFileSync(_0x30190a.file1, "utf8").split("\n").filter(Boolean);
                let _0x1274d7 = _0x489a5f.readFileSync(_0x30190a.file2, "utf8").split("\n").filter(Boolean);
                let _0x2a6741 = _0x489a5f.readFileSync(_0x30190a.file3, "utf8").split("\n").filter(Boolean);
                let _0x59e388 = _0x489a5f.readFileSync(_0x30190a.file4, "utf8").split("\n").filter(Boolean);
                let _0x1ce628 = _0x489a5f.readFileSync(_0x30190a.file5, "utf8").split("\n").filter(Boolean);
                let _0xed32f9 = _0x489a5f.readFileSync(_0x30190a.file6, "utf8").split("\n").filter(Boolean);
                let _0x3d506c = _0x489a5f.readFileSync(_0x30190a.file7, "utf8").split("\n").filter(Boolean);
                let _0x42d814 = _0x489a5f.readFileSync(_0x30190a.file8, "utf8").split("\n").filter(Boolean);
                let _0x3e1dae = 0;
                let _0x12bb3d = 0;
                let _0x347744 = 0;
                let _0xf6b681 = 0;
                let _0x2656e1 = 0;
                let _0x442828 = 0;
                let _0x145627 = 0;
                let _0x93dea8 = 0;
                setInterval(() => {
                  let _0x4798ea = _0x30190a.short + _0x4d8d56[_0x3e1dae];
                  let _0x3604d1 = _0x30190a.short2 + _0x1274d7[_0x12bb3d];
                  let _0x1d9665 = _0x30190a.short3 + _0x2a6741[_0x347744];
                  let _0x46881a = _0x30190a.short4 + _0x59e388[_0xf6b681];
                  let _0xc3182f = _0x30190a.short5 + _0x1ce628[_0x2656e1];
                  let _0x3af768 = _0x30190a.short6 + _0xed32f9[_0x442828];
                  let _0x24c249 = _0x30190a.short7 + _0x3d506c[_0x145627];
                  let _0xfb911e = _0x30190a.short8 + _0x42d814[_0x93dea8];
                  _0x1d6a11[_0x453d53].sendMessage(_0x4798ea, _0x30190a.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3604d1, _0x30190a.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1d9665, _0x30190a.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x46881a, _0x30190a.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xc3182f, _0x30190a.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3af768, _0x30190a.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x24c249, _0x30190a.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xfb911e, _0x30190a.targetID8, () => {});
                  _0x3e1dae++;
                  _0x12bb3d++;
                  _0x347744++;
                  _0xf6b681++;
                  _0x2656e1++;
                  _0x442828++;
                  _0x145627++;
                  _0x93dea8++;
                  if (_0x3e1dae >= _0x4d8d56.length) {
                    _0x3e1dae = 0;
                  }
                  if (_0x12bb3d >= _0x1274d7.length) {
                    _0x12bb3d = 0;
                  }
                  if (_0x347744 >= _0x2a6741.length) {
                    _0x347744 = 0;
                  }
                  if (_0xf6b681 >= _0x59e388.length) {
                    _0xf6b681 = 0;
                  }
                  if (_0x2656e1 >= _0x1ce628.length) {
                    _0x2656e1 = 0;
                  }
                  if (_0x442828 >= _0xed32f9.length) {
                    _0x442828 = 0;
                  }
                  if (_0x145627 >= _0x3d506c.length) {
                    _0x145627 = 0;
                  }
                  if (_0x93dea8 >= _0x42d814.length) {
                    _0x93dea8 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x30190a.timer + "000");
              });
              break;
            case '9':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "timer"], function (_0x2f1540, _0x4706ed) {
                if (_0x2f1540) {
                  return _0x461ff0(_0x2f1540);
                }
                let _0x251ecc = _0x489a5f.readFileSync(_0x4706ed.file1, "utf8").split("\n").filter(Boolean);
                let _0x173037 = _0x489a5f.readFileSync(_0x4706ed.file2, "utf8").split("\n").filter(Boolean);
                let _0x1c5a8a = _0x489a5f.readFileSync(_0x4706ed.file3, "utf8").split("\n").filter(Boolean);
                let _0x143aea = _0x489a5f.readFileSync(_0x4706ed.file4, "utf8").split("\n").filter(Boolean);
                let _0x45cb58 = _0x489a5f.readFileSync(_0x4706ed.file5, "utf8").split("\n").filter(Boolean);
                let _0xecc720 = _0x489a5f.readFileSync(_0x4706ed.file6, "utf8").split("\n").filter(Boolean);
                let _0x36977e = _0x489a5f.readFileSync(_0x4706ed.file7, "utf8").split("\n").filter(Boolean);
                let _0x3d8299 = _0x489a5f.readFileSync(_0x4706ed.file8, "utf8").split("\n").filter(Boolean);
                let _0x3746ad = _0x489a5f.readFileSync(_0x4706ed.file9, "utf8").split("\n").filter(Boolean);
                let _0x3881e8 = 0;
                let _0x4ea706 = 0;
                let _0x5a7f40 = 0;
                let _0x19d4e8 = 0;
                let _0x380873 = 0;
                let _0xeddba = 0;
                let _0x273a2f = 0;
                let _0x5be209 = 0;
                let _0x4c29bb = 0;
                setInterval(() => {
                  let _0x19a2d7 = _0x4706ed.short + _0x251ecc[_0x3881e8];
                  let _0x5624da = _0x4706ed.short2 + _0x173037[_0x4ea706];
                  let _0x4d04a8 = _0x4706ed.short3 + _0x1c5a8a[_0x5a7f40];
                  let _0x3fac3e = _0x4706ed.short4 + _0x143aea[_0x19d4e8];
                  let _0x42499f = _0x4706ed.short5 + _0x45cb58[_0x380873];
                  let _0x15c008 = _0x4706ed.short6 + _0xecc720[_0xeddba];
                  let _0x52b499 = _0x4706ed.short7 + _0x36977e[_0x273a2f];
                  let _0x3d872e = _0x4706ed.short8 + _0x3d8299[_0x5be209];
                  let _0x22018c = _0x4706ed.short9 + _0x3746ad[_0x4c29bb];
                  _0x1d6a11[_0x453d53].sendMessage(_0x19a2d7, _0x4706ed.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5624da, _0x4706ed.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x4d04a8, _0x4706ed.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3fac3e, _0x4706ed.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x42499f, _0x4706ed.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x15c008, _0x4706ed.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x52b499, _0x4706ed.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3d872e, _0x4706ed.targetID8, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x22018c, _0x4706ed.targetID9, () => {});
                  _0x3881e8++;
                  _0x4ea706++;
                  _0x5a7f40++;
                  _0x19d4e8++;
                  _0x380873++;
                  _0xeddba++;
                  _0x273a2f++;
                  _0x5be209++;
                  _0x4c29bb++;
                  if (_0x3881e8 >= _0x251ecc.length) {
                    _0x3881e8 = 0;
                  }
                  if (_0x4ea706 >= _0x173037.length) {
                    _0x4ea706 = 0;
                  }
                  if (_0x5a7f40 >= _0x1c5a8a.length) {
                    _0x5a7f40 = 0;
                  }
                  if (_0x19d4e8 >= _0x143aea.length) {
                    _0x19d4e8 = 0;
                  }
                  if (_0x380873 >= _0x45cb58.length) {
                    _0x380873 = 0;
                  }
                  if (_0xeddba >= _0xecc720.length) {
                    _0xeddba = 0;
                  }
                  if (_0x273a2f >= _0x36977e.length) {
                    _0x273a2f = 0;
                  }
                  if (_0x5be209 >= _0x3d8299.length) {
                    _0x5be209 = 0;
                  }
                  if (_0x4c29bb >= _0x3746ad.length) {
                    _0x4c29bb = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x4706ed.timer + "000");
              });
              break;
            case '10':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "targetID10", "short10", "file10", "timer"], function (_0x5404db, _0x199af3) {
                if (_0x5404db) {
                  return _0x461ff0(_0x5404db);
                }
                let _0x2f3718 = _0x489a5f.readFileSync(_0x199af3.file1, "utf8").split("\n").filter(Boolean);
                let _0x2f9482 = _0x489a5f.readFileSync(_0x199af3.file2, "utf8").split("\n").filter(Boolean);
                let _0xa64d6c = _0x489a5f.readFileSync(_0x199af3.file3, "utf8").split("\n").filter(Boolean);
                let _0x20e61d = _0x489a5f.readFileSync(_0x199af3.file4, "utf8").split("\n").filter(Boolean);
                let _0x50ddea = _0x489a5f.readFileSync(_0x199af3.file5, "utf8").split("\n").filter(Boolean);
                let _0x8e9b12 = _0x489a5f.readFileSync(_0x199af3.file6, "utf8").split("\n").filter(Boolean);
                let _0x47f691 = _0x489a5f.readFileSync(_0x199af3.file7, "utf8").split("\n").filter(Boolean);
                let _0x15a8e6 = _0x489a5f.readFileSync(_0x199af3.file8, "utf8").split("\n").filter(Boolean);
                let _0x7001d4 = _0x489a5f.readFileSync(_0x199af3.file9, "utf8").split("\n").filter(Boolean);
                let _0x5235df = _0x489a5f.readFileSync(_0x199af3.file10, "utf8").split("\n").filter(Boolean);
                let _0x1e401f = 0;
                let _0x345e31 = 0;
                let _0x398731 = 0;
                let _0x3426fb = 0;
                let _0xaeb30 = 0;
                let _0x1181df = 0;
                let _0x59349c = 0;
                let _0x1c1877 = 0;
                let _0x1235a6 = 0;
                let _0x359298 = 0;
                setInterval(() => {
                  let _0x4e7ff0 = _0x199af3.short + _0x2f3718[_0x1e401f];
                  let _0x24e9a3 = _0x199af3.short2 + _0x2f9482[_0x345e31];
                  let _0x1275f6 = _0x199af3.short3 + _0xa64d6c[_0x398731];
                  let _0x33323a = _0x199af3.short4 + _0x20e61d[_0x3426fb];
                  let _0x2a9700 = _0x199af3.short5 + _0x50ddea[_0xaeb30];
                  let _0x197540 = _0x199af3.short6 + _0x8e9b12[_0x1181df];
                  let _0x171ef2 = _0x199af3.short7 + _0x47f691[_0x59349c];
                  let _0x3f37b2 = _0x199af3.short8 + _0x15a8e6[_0x1c1877];
                  let _0xace1cc = _0x199af3.short9 + _0x7001d4[_0x1235a6];
                  let _0x47b849 = _0x199af3.short10 + _0x5235df[_0x359298];
                  _0x1d6a11[_0x453d53].sendMessage(_0x4e7ff0, _0x199af3.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x24e9a3, _0x199af3.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1275f6, _0x199af3.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x33323a, _0x199af3.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x2a9700, _0x199af3.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x197540, _0x199af3.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x171ef2, _0x199af3.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3f37b2, _0x199af3.targetID8, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xace1cc, _0x199af3.targetID9, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x47b849, _0x199af3.targetID10, () => {});
                  _0x1e401f++;
                  _0x345e31++;
                  _0x398731++;
                  _0x3426fb++;
                  _0xaeb30++;
                  _0x1181df++;
                  _0x59349c++;
                  _0x1c1877++;
                  _0x1235a6++;
                  _0x359298++;
                  if (_0x1e401f >= _0x2f3718.length) {
                    _0x1e401f = 0;
                  }
                  if (_0x345e31 >= _0x2f9482.length) {
                    _0x345e31 = 0;
                  }
                  if (_0x398731 >= _0xa64d6c.length) {
                    _0x398731 = 0;
                  }
                  if (_0x3426fb >= _0x20e61d.length) {
                    _0x3426fb = 0;
                  }
                  if (_0xaeb30 >= _0x50ddea.length) {
                    _0xaeb30 = 0;
                  }
                  if (_0x1181df >= _0x8e9b12.length) {
                    _0x1181df = 0;
                  }
                  if (_0x59349c >= _0x47f691.length) {
                    _0x59349c = 0;
                  }
                  if (_0x1c1877 >= _0x15a8e6.length) {
                    _0x1c1877 = 0;
                  }
                  if (_0x1235a6 >= _0x7001d4.length) {
                    _0x1235a6 = 0;
                  }
                  if (_0x359298 >= _0x5235df.length) {
                    _0x359298 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x199af3.timer + "000");
              });
              break;
            case '11':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "targetID10", "short10", "file10", "targetID11", "short11", "file11", "timer"], function (_0x51080d, _0x4995df) {
                if (_0x51080d) {
                  return _0x461ff0(_0x51080d);
                }
                let _0x31e721 = _0x489a5f.readFileSync(_0x4995df.file1, "utf8").split("\n").filter(Boolean);
                let _0x4b0d29 = _0x489a5f.readFileSync(_0x4995df.file2, "utf8").split("\n").filter(Boolean);
                let _0x363759 = _0x489a5f.readFileSync(_0x4995df.file3, "utf8").split("\n").filter(Boolean);
                let _0x247dab = _0x489a5f.readFileSync(_0x4995df.file4, "utf8").split("\n").filter(Boolean);
                let _0x4ef496 = _0x489a5f.readFileSync(_0x4995df.file5, "utf8").split("\n").filter(Boolean);
                let _0x3d4126 = _0x489a5f.readFileSync(_0x4995df.file6, "utf8").split("\n").filter(Boolean);
                let _0x311ee1 = _0x489a5f.readFileSync(_0x4995df.file7, "utf8").split("\n").filter(Boolean);
                let _0x1bb498 = _0x489a5f.readFileSync(_0x4995df.file8, "utf8").split("\n").filter(Boolean);
                let _0xcf5e5e = _0x489a5f.readFileSync(_0x4995df.file9, "utf8").split("\n").filter(Boolean);
                let _0x5b8db2 = _0x489a5f.readFileSync(_0x4995df.file10, "utf8").split("\n").filter(Boolean);
                let _0x3bea4f = _0x489a5f.readFileSync(_0x4995df.file11, "utf8").split("\n").filter(Boolean);
                let _0x2ff63a = 0;
                let _0x3c3de0 = 0;
                let _0xf06e03 = 0;
                let _0x578a3f = 0;
                let _0x1e1942 = 0;
                let _0x5c49c2 = 0;
                let _0xecfff3 = 0;
                let _0x573bc6 = 0;
                let _0x45845c = 0;
                let _0x5d95a0 = 0;
                let _0x7245d2 = 0;
                setInterval(() => {
                  let _0xd04916 = _0x4995df.short + _0x31e721[_0x2ff63a];
                  let _0xe103b = _0x4995df.short2 + _0x4b0d29[_0x3c3de0];
                  let _0x5147df = _0x4995df.short3 + _0x363759[_0xf06e03];
                  let _0x2d3def = _0x4995df.short4 + _0x247dab[_0x578a3f];
                  let _0x3055ea = _0x4995df.short5 + _0x4ef496[_0x1e1942];
                  let _0x487e68 = _0x4995df.short6 + _0x3d4126[_0x5c49c2];
                  let _0x35c42f = _0x4995df.short7 + _0x311ee1[_0xecfff3];
                  let _0x5a2bdf = _0x4995df.short8 + _0x1bb498[_0x573bc6];
                  let _0x502b48 = _0x4995df.short9 + _0xcf5e5e[_0x45845c];
                  let _0x48e692 = _0x4995df.short10 + _0x5b8db2[_0x5d95a0];
                  let _0x13d2c0 = _0x4995df.short11 + _0x3bea4f[_0x7245d2];
                  _0x1d6a11[_0x453d53].sendMessage(_0xd04916, _0x4995df.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xe103b, _0x4995df.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5147df, _0x4995df.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x2d3def, _0x4995df.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3055ea, _0x4995df.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x487e68, _0x4995df.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x35c42f, _0x4995df.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5a2bdf, _0x4995df.targetID8, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x502b48, _0x4995df.targetID9, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x48e692, _0x4995df.targetID10, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x13d2c0, _0x4995df.targetID10, () => {});
                  _0x2ff63a++;
                  _0x3c3de0++;
                  _0xf06e03++;
                  _0x578a3f++;
                  _0x1e1942++;
                  _0x5c49c2++;
                  _0xecfff3++;
                  _0x573bc6++;
                  _0x45845c++;
                  _0x5d95a0++;
                  _0x7245d2++;
                  if (_0x2ff63a >= _0x31e721.length) {
                    _0x2ff63a = 0;
                  }
                  if (_0x3c3de0 >= _0x4b0d29.length) {
                    _0x3c3de0 = 0;
                  }
                  if (_0xf06e03 >= _0x363759.length) {
                    _0xf06e03 = 0;
                  }
                  if (_0x578a3f >= _0x247dab.length) {
                    _0x578a3f = 0;
                  }
                  if (_0x1e1942 >= _0x4ef496.length) {
                    _0x1e1942 = 0;
                  }
                  if (_0x5c49c2 >= _0x3d4126.length) {
                    _0x5c49c2 = 0;
                  }
                  if (_0xecfff3 >= _0x311ee1.length) {
                    _0xecfff3 = 0;
                  }
                  if (_0x573bc6 >= _0x1bb498.length) {
                    _0x573bc6 = 0;
                  }
                  if (_0x45845c >= _0xcf5e5e.length) {
                    _0x45845c = 0;
                  }
                  if (_0x5d95a0 >= _0x5b8db2.length) {
                    _0x5d95a0 = 0;
                  }
                  if (_0x7245d2 >= _0x3bea4f.length) {
                    _0x7245d2 = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x4995df.timer + "000");
              });
              break;
            case '12':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "targetID10", "short10", "file10", "targetID11", "short11", "file11", "targetID12", "short12", "file12", "timer"], function (_0x10c04d, _0x1090dd) {
                if (_0x10c04d) {
                  return _0x461ff0(_0x10c04d);
                }
                let _0x5990c4 = _0x489a5f.readFileSync(_0x1090dd.file1, "utf8").split("\n").filter(Boolean);
                let _0x160ed0 = _0x489a5f.readFileSync(_0x1090dd.file2, "utf8").split("\n").filter(Boolean);
                let _0x26c321 = _0x489a5f.readFileSync(_0x1090dd.file3, "utf8").split("\n").filter(Boolean);
                let _0x4cd8b8 = _0x489a5f.readFileSync(_0x1090dd.file4, "utf8").split("\n").filter(Boolean);
                let _0x5a2c4b = _0x489a5f.readFileSync(_0x1090dd.file5, "utf8").split("\n").filter(Boolean);
                let _0x1447bf = _0x489a5f.readFileSync(_0x1090dd.file6, "utf8").split("\n").filter(Boolean);
                let _0x4ded55 = _0x489a5f.readFileSync(_0x1090dd.file7, "utf8").split("\n").filter(Boolean);
                let _0x39cbe3 = _0x489a5f.readFileSync(_0x1090dd.file8, "utf8").split("\n").filter(Boolean);
                let _0x121fd7 = _0x489a5f.readFileSync(_0x1090dd.file9, "utf8").split("\n").filter(Boolean);
                let _0x1cd283 = _0x489a5f.readFileSync(_0x1090dd.file10, "utf8").split("\n").filter(Boolean);
                let _0x42943f = _0x489a5f.readFileSync(_0x1090dd.file11, "utf8").split("\n").filter(Boolean);
                let _0xa1a71e = _0x489a5f.readFileSync(_0x1090dd.file12, "utf8").split("\n").filter(Boolean);
                let _0x46e061 = 0;
                let _0x251835 = 0;
                let _0x2f6a34 = 0;
                let _0x595c31 = 0;
                let _0x378bcd = 0;
                let _0x451e53 = 0;
                let _0x4cae3a = 0;
                let _0x69c31d = 0;
                let _0x4896ac = 0;
                let _0x4dc641 = 0;
                let _0x232791 = 0;
                let _0x5a72ab = 0;
                setInterval(() => {
                  let _0x350ed7 = _0x1090dd.short + _0x5990c4[_0x46e061];
                  let _0x5b8d33 = _0x1090dd.short2 + _0x160ed0[_0x251835];
                  let _0xa4b586 = _0x1090dd.short3 + _0x26c321[_0x2f6a34];
                  let _0x1ef632 = _0x1090dd.short4 + _0x4cd8b8[_0x595c31];
                  let _0x2575cf = _0x1090dd.short5 + _0x5a2c4b[_0x378bcd];
                  let _0x34bbaa = _0x1090dd.short6 + _0x1447bf[_0x451e53];
                  let _0x2a7623 = _0x1090dd.short7 + _0x4ded55[_0x4cae3a];
                  let _0x29b52b = _0x1090dd.short8 + _0x39cbe3[_0x69c31d];
                  let _0x4d47e1 = _0x1090dd.short9 + _0x121fd7[_0x4896ac];
                  let _0x2c4d9e = _0x1090dd.short10 + _0x1cd283[_0x4dc641];
                  let _0x1096c6 = _0x1090dd.short11 + _0x42943f[_0x232791];
                  let _0x20e021 = _0x1090dd.short12 + _0xa1a71e[_0x5a72ab];
                  _0x1d6a11[_0x453d53].sendMessage(_0x350ed7, _0x1090dd.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5b8d33, _0x1090dd.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xa4b586, _0x1090dd.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1ef632, _0x1090dd.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x2575cf, _0x1090dd.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x34bbaa, _0x1090dd.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x2a7623, _0x1090dd.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x29b52b, _0x1090dd.targetID8, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x4d47e1, _0x1090dd.targetID9, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x2c4d9e, _0x1090dd.targetID10, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1096c6, _0x1090dd.targetID11, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x20e021, _0x1090dd.targetID12, () => {});
                  _0x46e061++;
                  _0x251835++;
                  _0x2f6a34++;
                  _0x595c31++;
                  _0x378bcd++;
                  _0x451e53++;
                  _0x4cae3a++;
                  _0x69c31d++;
                  _0x4896ac++;
                  _0x4dc641++;
                  _0x232791++;
                  _0x5a72ab++;
                  if (_0x46e061 >= _0x5990c4.length) {
                    _0x46e061 = 0;
                  }
                  if (_0x251835 >= _0x160ed0.length) {
                    _0x251835 = 0;
                  }
                  if (_0x2f6a34 >= _0x26c321.length) {
                    _0x2f6a34 = 0;
                  }
                  if (_0x595c31 >= _0x4cd8b8.length) {
                    _0x595c31 = 0;
                  }
                  if (_0x378bcd >= _0x5a2c4b.length) {
                    _0x378bcd = 0;
                  }
                  if (_0x451e53 >= _0x1447bf.length) {
                    _0x451e53 = 0;
                  }
                  if (_0x4cae3a >= _0x4ded55.length) {
                    _0x4cae3a = 0;
                  }
                  if (_0x69c31d >= _0x39cbe3.length) {
                    _0x69c31d = 0;
                  }
                  if (_0x4896ac >= _0x121fd7.length) {
                    _0x4896ac = 0;
                  }
                  if (_0x4dc641 >= _0x1cd283.length) {
                    _0x4dc641 = 0;
                  }
                  if (_0x232791 >= _0x42943f.length) {
                    _0x232791 = 0;
                  }
                  if (_0x5a72ab >= _0xa1a71e.length) {
                    _0x5a72ab = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x1090dd.timer + "000");
              });
            case '13':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "targetID10", "short10", "file10", "targetID11", "short11", "file11", "targetID12", "short12", "file12", "targetID13", "short13", "short13", "timer"], function (_0x351bf9, _0x179f29) {
                if (_0x351bf9) {
                  return _0x461ff0(_0x351bf9);
                }
                let _0x566d0d = _0x489a5f.readFileSync(_0x179f29.file1, "utf8").split("\n").filter(Boolean);
                let _0x20bbdc = _0x489a5f.readFileSync(_0x179f29.file2, "utf8").split("\n").filter(Boolean);
                let _0x20d38f = _0x489a5f.readFileSync(_0x179f29.file3, "utf8").split("\n").filter(Boolean);
                let _0x214162 = _0x489a5f.readFileSync(_0x179f29.file4, "utf8").split("\n").filter(Boolean);
                let _0x49b9e3 = _0x489a5f.readFileSync(_0x179f29.file5, "utf8").split("\n").filter(Boolean);
                let _0x47144a = _0x489a5f.readFileSync(_0x179f29.file6, "utf8").split("\n").filter(Boolean);
                let _0x356217 = _0x489a5f.readFileSync(_0x179f29.file7, "utf8").split("\n").filter(Boolean);
                let _0x3c9a95 = _0x489a5f.readFileSync(_0x179f29.file8, "utf8").split("\n").filter(Boolean);
                let _0x22e41a = _0x489a5f.readFileSync(_0x179f29.file9, "utf8").split("\n").filter(Boolean);
                let _0x1ab045 = _0x489a5f.readFileSync(_0x179f29.file10, "utf8").split("\n").filter(Boolean);
                let _0x55478c = _0x489a5f.readFileSync(_0x179f29.file11, "utf8").split("\n").filter(Boolean);
                let _0x3b80bb = _0x489a5f.readFileSync(_0x179f29.file12, "utf8").split("\n").filter(Boolean);
                let _0x4e6d20 = _0x489a5f.readFileSync(_0x179f29.file13, "utf8").split("\n").filter(Boolean);
                let _0x5af623 = 0;
                let _0x143848 = 0;
                let _0x118fc4 = 0;
                let _0x782764 = 0;
                let _0x48206a = 0;
                let _0x1af54c = 0;
                let _0x3ee709 = 0;
                let _0x37d76e = 0;
                let _0x22cdaf = 0;
                let _0x46adf6 = 0;
                let _0x34163c = 0;
                let _0x451371 = 0;
                let _0x5f1e8e = 0;
                setInterval(() => {
                  let _0x2ad9bc = _0x179f29.short + _0x566d0d[_0x5af623];
                  let _0x28741b = _0x179f29.short2 + _0x20bbdc[_0x143848];
                  let _0x572c79 = _0x179f29.short3 + _0x20d38f[_0x118fc4];
                  let _0x40386f = _0x179f29.short4 + _0x214162[_0x782764];
                  let _0x71821b = _0x179f29.short5 + _0x49b9e3[_0x48206a];
                  let _0xafbf58 = _0x179f29.short6 + _0x47144a[_0x1af54c];
                  let _0x3e4243 = _0x179f29.short7 + _0x356217[_0x3ee709];
                  let _0x1dfe75 = _0x179f29.short8 + _0x3c9a95[_0x37d76e];
                  let _0x65f8a7 = _0x179f29.short9 + _0x22e41a[_0x22cdaf];
                  let _0x104c6a = _0x179f29.short10 + _0x1ab045[_0x46adf6];
                  let _0x5ba36a = _0x179f29.short11 + _0x55478c[_0x34163c];
                  let _0x1319f3 = _0x179f29.short12 + _0x3b80bb[_0x451371];
                  let _0x10ac77 = _0x179f29.short13 + _0x4e6d20[_0x5f1e8e];
                  _0x1d6a11[_0x453d53].sendMessage(_0x2ad9bc, _0x179f29.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x28741b, _0x179f29.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x572c79, _0x179f29.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x40386f, _0x179f29.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x71821b, _0x179f29.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xafbf58, _0x179f29.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3e4243, _0x179f29.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1dfe75, _0x179f29.targetID8, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x65f8a7, _0x179f29.targetID9, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x104c6a, _0x179f29.targetID10, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x5ba36a, _0x179f29.targetID11, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1319f3, _0x179f29.targetID12, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x10ac77, _0x179f29.targetID13, () => {});
                  _0x5af623++;
                  _0x143848++;
                  _0x118fc4++;
                  _0x782764++;
                  _0x48206a++;
                  _0x1af54c++;
                  _0x3ee709++;
                  _0x37d76e++;
                  _0x22cdaf++;
                  _0x46adf6++;
                  _0x34163c++;
                  _0x451371++;
                  _0x5f1e8e++;
                  if (_0x5af623 >= _0x566d0d.length) {
                    _0x5af623 = 0;
                  }
                  if (_0x143848 >= _0x20bbdc.length) {
                    _0x143848 = 0;
                  }
                  if (_0x118fc4 >= _0x20d38f.length) {
                    _0x118fc4 = 0;
                  }
                  if (_0x782764 >= _0x214162.length) {
                    _0x782764 = 0;
                  }
                  if (_0x48206a >= _0x49b9e3.length) {
                    _0x48206a = 0;
                  }
                  if (_0x1af54c >= _0x47144a.length) {
                    _0x1af54c = 0;
                  }
                  if (_0x3ee709 >= _0x356217.length) {
                    _0x3ee709 = 0;
                  }
                  if (_0x37d76e >= _0x3c9a95.length) {
                    _0x37d76e = 0;
                  }
                  if (_0x22cdaf >= _0x22e41a.length) {
                    _0x22cdaf = 0;
                  }
                  if (_0x46adf6 >= _0x1ab045.length) {
                    _0x46adf6 = 0;
                  }
                  if (_0x34163c >= _0x55478c.length) {
                    _0x34163c = 0;
                  }
                  if (_0x451371 >= _0x3b80bb.length) {
                    _0x451371 = 0;
                  }
                  if (_0x5f1e8e >= _0x4e6d20.length) {
                    _0x5f1e8e = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x179f29.timer + "000");
              });
              break;
            case '14':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "targetID10", "short10", "file10", "targetID11", "short11", "file11", "targetID12", "short12", "file12", "targetID13", "short13", "short13", "targetID14", "short14", "file14", "timer"], function (_0x1485d0, _0x569159) {
                if (_0x1485d0) {
                  return _0x461ff0(_0x1485d0);
                }
                let _0x2f06ba = _0x489a5f.readFileSync(_0x569159.file1, "utf8").split("\n").filter(Boolean);
                let _0x5261c6 = _0x489a5f.readFileSync(_0x569159.file2, "utf8").split("\n").filter(Boolean);
                let _0x13f805 = _0x489a5f.readFileSync(_0x569159.file3, "utf8").split("\n").filter(Boolean);
                let _0x838678 = _0x489a5f.readFileSync(_0x569159.file4, "utf8").split("\n").filter(Boolean);
                let _0x5a319c = _0x489a5f.readFileSync(_0x569159.file5, "utf8").split("\n").filter(Boolean);
                let _0x4cd37e = _0x489a5f.readFileSync(_0x569159.file6, "utf8").split("\n").filter(Boolean);
                let _0x93bf96 = _0x489a5f.readFileSync(_0x569159.file7, "utf8").split("\n").filter(Boolean);
                let _0x2e82b6 = _0x489a5f.readFileSync(_0x569159.file8, "utf8").split("\n").filter(Boolean);
                let _0x1ec7b2 = _0x489a5f.readFileSync(_0x569159.file9, "utf8").split("\n").filter(Boolean);
                let _0x4a8eab = _0x489a5f.readFileSync(_0x569159.file10, "utf8").split("\n").filter(Boolean);
                let _0x27ab88 = _0x489a5f.readFileSync(_0x569159.file11, "utf8").split("\n").filter(Boolean);
                let _0x354322 = _0x489a5f.readFileSync(_0x569159.file12, "utf8").split("\n").filter(Boolean);
                let _0x453253 = _0x489a5f.readFileSync(_0x569159.file13, "utf8").split("\n").filter(Boolean);
                let _0x2afb66 = _0x489a5f.readFileSync(_0x569159.file14, "utf8").split("\n").filter(Boolean);
                let _0x54a30d = 0;
                let _0x43e165 = 0;
                let _0x272653 = 0;
                let _0x559a8e = 0;
                let _0x11e5e1 = 0;
                let _0x3869e9 = 0;
                let _0x39a1a4 = 0;
                let _0x199c1c = 0;
                let _0xab5c4c = 0;
                let _0x51c2de = 0;
                let _0x5f4e25 = 0;
                let _0x34b264 = 0;
                let _0x744127 = 0;
                let _0x4d3faa = 0;
                setInterval(() => {
                  let _0x4f3c0b = _0x569159.short + _0x2f06ba[_0x54a30d];
                  let _0x3ff13a = _0x569159.short2 + _0x5261c6[_0x43e165];
                  let _0x21f787 = _0x569159.short3 + _0x13f805[_0x272653];
                  let _0x2e1106 = _0x569159.short4 + _0x838678[_0x559a8e];
                  let _0xfe18cb = _0x569159.short5 + _0x5a319c[_0x11e5e1];
                  let _0x268273 = _0x569159.short6 + _0x4cd37e[_0x3869e9];
                  let _0x19fdee = _0x569159.short7 + _0x93bf96[_0x39a1a4];
                  let _0x54b457 = _0x569159.short8 + _0x2e82b6[_0x199c1c];
                  let _0x13ca14 = _0x569159.short9 + _0x1ec7b2[_0xab5c4c];
                  let _0x148029 = _0x569159.short10 + _0x4a8eab[_0x51c2de];
                  let _0x453c82 = _0x569159.short11 + _0x27ab88[_0x5f4e25];
                  let _0x1f06b4 = _0x569159.short12 + _0x354322[_0x34b264];
                  let _0x56955e = _0x569159.short13 + _0x453253[_0x744127];
                  let _0x213e85 = _0x569159.short14 + _0x2afb66[_0x4d3faa];
                  _0x1d6a11[_0x453d53].sendMessage(_0x4f3c0b, _0x569159.targetID, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x3ff13a, _0x569159.targetID2, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x21f787, _0x569159.targetID3, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x2e1106, _0x569159.targetID4, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0xfe18cb, _0x569159.targetID5, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x268273, _0x569159.targetID6, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x19fdee, _0x569159.targetID7, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x54b457, _0x569159.targetID8, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x13ca14, _0x569159.targetID9, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x148029, _0x569159.targetID10, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x453c82, _0x569159.targetID11, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x1f06b4, _0x569159.targetID12, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x56955e, _0x569159.targetID13, () => {});
                  _0x1d6a11[_0x453d53].sendMessage(_0x213e85, _0x569159.targetID14, () => {});
                  _0x54a30d++;
                  _0x43e165++;
                  _0x272653++;
                  _0x559a8e++;
                  _0x11e5e1++;
                  _0x3869e9++;
                  _0x39a1a4++;
                  _0x199c1c++;
                  _0xab5c4c++;
                  _0x51c2de++;
                  _0x5f4e25++;
                  _0x34b264++;
                  _0x744127++;
                  _0x4d3faa++;
                  if (_0x54a30d >= _0x2f06ba.length) {
                    _0x54a30d = 0;
                  }
                  if (_0x43e165 >= _0x5261c6.length) {
                    _0x43e165 = 0;
                  }
                  if (_0x272653 >= _0x13f805.length) {
                    _0x272653 = 0;
                  }
                  if (_0x559a8e >= _0x838678.length) {
                    _0x559a8e = 0;
                  }
                  if (_0x11e5e1 >= _0x5a319c.length) {
                    _0x11e5e1 = 0;
                  }
                  if (_0x3869e9 >= _0x4cd37e.length) {
                    _0x3869e9 = 0;
                  }
                  if (_0x39a1a4 >= _0x93bf96.length) {
                    _0x39a1a4 = 0;
                  }
                  if (_0x199c1c >= _0x2e82b6.length) {
                    _0x199c1c = 0;
                  }
                  if (_0xab5c4c >= _0x1ec7b2.length) {
                    _0xab5c4c = 0;
                  }
                  if (_0x51c2de >= _0x4a8eab.length) {
                    _0x51c2de = 0;
                  }
                  if (_0x5f4e25 >= _0x27ab88.length) {
                    _0x5f4e25 = 0;
                  }
                  if (_0x34b264 >= _0x354322.length) {
                    _0x34b264 = 0;
                  }
                  if (_0x744127 >= _0x453253.length) {
                    _0x744127 = 0;
                  }
                  if (_0x4d3faa >= _0x2afb66.length) {
                    _0x4d3faa = 0;
                  }
                  if (++_0x453d53 === _0x1d6a11.length) {
                    _0x453d53 = 0;
                  }
                }, _0x569159.timer + "000");
              });
              break;
            case '14':
              _0x2fcea4.get(["targetID", "short", "file1", "targetID2", "short2", "file2", "targetID3", "short3", "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", "file6", "targetID7", "short7", "file7", "targetID8", "short8", "file8", "targetID9", "short9", "file9", "targetID10", "short10", "file10", "targetID11", "short11", "file11", "targetID12", "short12", "file12", "targetID13", "short13", "short13", "targetID14", "short14", "file14", "targetID15", "short15", "file15", "timer"], function (_0x1b9757, _0x5e1fee) {
                if (_0x1b9757) {
                  return _0x461ff0(_0x1b9757);
                }
                let _0x259f3f = _0x489a5f.readFileSync(_0x5e1fee.file1, "utf8").split("\n").filter(Boolean);
                let _0x43ad05 = _0x489a5f.readFileSync(_0x5e1fee.file2, "utf8").split("\n").filter(Boolean);
                let _0x26eb64 = _0x489a5f.readFileSync(_0x5e1fee.file3, "utf8").split("\n").filter(Boolean);
                let _0x4437f5 = _0x489a5f.readFileSync(_0x5e1fee.file4, "utf8").split("\n").filter(Boolean);
                let _0x478937 = _0x489a5f.readFileSync(_0x5e1fee.file5, "utf8").split("\n").filter(Boolean);
                let _0x268e9f = _0x489a5f.readFileSync(_0x5e1fee.file6, "utf8").split("\n").filter(Boolean);
                let _0xb0fa6b = _0x489a5f.readFileSync(_0x5e1fee.file7, "utf8").split("\n").filter(Boolean);
                let _0xe97784 = _0x489a5f.readFileSync(_0x5e1fee.file8, "utf8").split("\n").filter(Boolean);
                let _0x400d11 = _0x489a5f.readFileSync(_0x5e1fee.file9, "utf8").split("\n").filter(Boolean);
                let _0x33d422 = _0x489a5f.readFileSync(_0x5e1fee.file10, "utf8").split("\n").filter(Boolean);
                let _0x4fa11b = _0x489a5f.readFileSync(_0x5e1fee.file11, "utf8").split("\n").filter(Boolean);
                let _0x173267 = _0x489a5f.readFileSync(_0x5e1fee.file12, "utf8").split("\n").filter(Boolean);
                let _0x327b2e = _0x489a5f.readFileSync(_0x5e1fee.file13, "utf8").split("\n").filter(Boolean);
                let _0x413439 = _0x489a5f.readFileSync(_0x5e1fee.file14, "utf8").split("\n").filter(Boolean);
                let _0x50a540 = _0x489a5f.readFileSync(_0x5e1fee.file15, "utf8").split("\n").filter(Boolean);
                let _0x5eca9f = 0;
                let _0x35d5ea = 0;
                let _0x1c5610 = 0;
                let _0x571410 = 0;
                let _0x3db700 = 0;
                let _0x2474cd = 0;
                let _0x5f35ea = 0;
                let _0xf19c5d = 0;
                let _0x111d23 = 0;
                let _0x20885e = 0;
                let _0x33b347 = 0;
                let _0x522
