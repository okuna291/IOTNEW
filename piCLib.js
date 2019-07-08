/////////////LED//////
// const Gpio = require('pigpio').Gpio;
 
// const led = new Gpio(17, {mode: Gpio.OUTPUT});
 
// let dutyCycle = 0;
 
// setInterval(() => {
//   led.pwmWrite(dutyCycle);
 
//   dutyCycle += 5;
//   if (dutyCycle > 255) {
//     dutyCycle = 0;
//   }
// }, 20);

/////////////SERVO//////
const Gpio = require('pigpio').Gpio;
 
const motor = new Gpio(17, {mode: Gpio.OUTPUT});
 
let pulseWidth = 1000;
let increment = 100;
 
setInterval(() => {
  motor.servoWrite(pulseWidth);
 
  pulseWidth += increment;
  if (pulseWidth >= 2000) {
    increment = -100;
  } else if (pulseWidth <= 1000) {
    increment = 100;
  }
}, 1000);