import express from 'express'
import handlebars from 'express-handlebars'
import __dirname from './utils.js'
import homeRouter from './router/homeRouter.js'
import menuRouter from './router/menuRouter.js'
import programRouter from './router/programRouter.js'

const port=8083
const app=express()
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use('/',express.static(__dirname+"/public"));

app.use('/',homeRouter)
app.use('/menu',menuRouter)
app.use('/program',programRouter)
//SET HANDLEABRS
app.engine('handlebars',handlebars.engine());
app.set('view engine',"handlebars");
app.set('views',__dirname+'/views');




app.listen(port,()=>{
    console.log(`app listening on port ${port}`)
}).on("error", function (err) {
    process.once("SIGUSR2", function () {
      process.kill(process.pid, "SIGUSR2");
    });
    process.on("SIGINT", function () {
      // this is only called on ctrl+c, not restart
      process.kill(process.pid, "SIGINT");
    });
  });

