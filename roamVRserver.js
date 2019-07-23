var finalhandler = require('finalhandler')
var http         = require('http')
var Router       = require('router')
const { Client } = require('node-osc');


var router = Router()
router.get('/', function (req, res) {
  res.setHeader('Content-Type', 'text/plain; charset=utf-8')
  res.end('Node Router! --- NOTHING TO SEE HERE')

})

router.get('/test', function (req, res) {
  res.setHeader('Content-Type', 'text/plain; charset=utf-8')
  res.end('You are in the test area!')
})

router.get('/value/:value', function(req, res) {
  res.end("the value entered is " +req.params.value);
});

router.get('/render/:xval/:yval/:zval', function(req, res) {
  res.end("XVAL= " + req.params.xval +" YVAL= "+ req.params.yval +" ZVAL= "+ req.params.zval);
});


router.get('/roamVR/:pid/:r0/:g0/:b0/:r1/:g1/:b1/:r2/:g2/:b2', function (req, res) {
  //javascript object
  var data = {
        "myvalues": {
          "p1d": req.params.pid,
            "r0": req.params.r0,
            "g0": req.params.g0,
            "b0": req.params.b0,
            "r1": req.params.r1,
            "g1": req.params.g1,
            "b1": req.params.b1,
            "r2": req.params.r2,
            "g2": req.params.g2,
            "b2": req.params.b2
        }
    }; 


  res.setHeader('Content-Type', 'text/plain; charset=utf-8')
  console.log(data);
  res.end("Values have been sent to server") 
 const client = new Client('127.0.0.1', 41234);
client.send('/foo', req.params.pid+"/"+req.params.r0+"/"+req.params.g0+"/"+req.params.b0+"/"+req.params.r1+"/"+req.params.g1+"/"+req.params.b1+"/"+req.params.r2+"/"+req.params.g2+"/"+req.params.b2 , () => {
  client.close();
});





 
});

// socket.on('/some/path', data => {
//   const msg = new OSC.Message()
//   msg.unpack(data)
//   console.log(msg.args)
// })
 
var server = http.createServer(function(req, res) {
  router(req, res, finalhandler(req, res))
})
 
server.listen(8000)