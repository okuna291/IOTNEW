var piblaster = require('pi-blaster.js');

piblaster.setPwm(17, 1 ); // 100% brightness
piblaster.setPwm(22, 0.2 ); // 20% brightness
piblaster.setPwm(23, 0 ); // off