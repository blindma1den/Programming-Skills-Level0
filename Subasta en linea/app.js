import express from "express"
import handlebars from "express-handlebars"
import __dirname from "./util.js";
import { CurrencyBank } from "./controllers/CurrencyBank.js";
import  currencyRouter  from "./router/bankRouter.js";

const currencyBank=new CurrencyBank("users.json","exchangerates.json");// => CREO EL BANCO QUE ALMACENARA LOS DATOS EN UN JSON

const app=express();
const port =8082

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use("/",express.static(__dirname+"/public"));
//ESTRUCTURA HANDLEBARS
app.engine('handlebars',handlebars.engine());
app.set('view engine','handlebars');
app.set('views',__dirname+"/public/views");

app.use("/",currencyRouter)


app.get('/',(req,res)=>{
    res.render('bank')
})

app.listen(port, () => {
    console.log('App listening on port 8082!');
}).on("error", function (err) {
    process.once("SIGUSR2", function () {
      process.kill(process.pid, "SIGUSR2");
    });
    process.on("SIGINT", function () {
      // this is only called on ctrl+c, not restart
      process.kill(process.pid, "SIGINT");
    });
  });

//console.log(__dirname)